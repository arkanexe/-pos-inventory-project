<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('branches', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('code', 32)->unique();
            $table->string('address')->nullable();
            $table->string('phone', 40)->nullable();
            $table->boolean('is_active')->default(true);
            $table->timestamps();
        });

        // Seed default head-office branch so existing records have a valid branch
        DB::table('branches')->insert([
            [
                'name' => 'Victoria Island Main Branch',
                'code' => 'BR-001',
                'address' => 'Plot 5, Commercial Block West, Victoria Island, Lagos',
                'phone' => '+234 1 270 0000',
                'is_active' => true,
                'created_at' => now(),
                'updated_at' => now(),
            ],
            [
                'name' => 'Ikeja Annex Branch',
                'code' => 'BR-002',
                'address' => '42 Allen Avenue, Ikeja, Lagos',
                'phone' => '+234 1 270 0001',
                'is_active' => true,
                'created_at' => now(),
                'updated_at' => now(),
            ],
        ]);
    }

    public function down(): void
    {
        Schema::dropIfExists('branches');
    }
};
