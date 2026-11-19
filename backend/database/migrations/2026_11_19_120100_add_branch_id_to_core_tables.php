<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        $tables = ['users', 'products', 'sales', 'stock_adjustments'];

        foreach ($tables as $tableName) {
            Schema::table($tableName, function (Blueprint $table) {
                $table->foreignId('branch_id')
                    ->nullable()
                    ->after('id')
                    ->constrained('branches')
                    ->nullOnDelete();
                $table->index('branch_id');
            });
        }

        // Assign existing records to the default branch (id=1) if it exists
        $defaultBranchId = DB::table('branches')->orderBy('id')->value('id');
        if ($defaultBranchId) {
            foreach ($tables as $tableName) {
                DB::table($tableName)
                    ->whereNull('branch_id')
                    ->update(['branch_id' => $defaultBranchId]);
            }
        }
    }

    public function down(): void
    {
        $tables = ['users', 'products', 'sales', 'stock_adjustments'];

        foreach ($tables as $tableName) {
            Schema::table($tableName, function (Blueprint $table) use ($tableName) {
                if (DB::getDriverName() !== 'sqlite') {
                    $table->dropForeign([$tableName === 'users' ? 'branch_id' : 'branch_id']);
                }
                $table->dropIndex(['branch_id']);
                $table->dropColumn('branch_id');
            });
        }
    }
};
