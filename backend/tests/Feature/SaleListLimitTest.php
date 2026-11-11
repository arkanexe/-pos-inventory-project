<?php

use App\Models\Sale;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;

uses(RefreshDatabase::class);

test('all sales response reports the true total when its 500 record payload is capped', function () {
    $owner = User::factory()->create(['role' => 'owner']);

    foreach (array_chunk(range(1, 501), 100) as $batch) {
        Sale::insert(array_map(fn () => [
            'user_id' => $owner->id,
            'payment_method' => 'cash',
            'subtotal' => 100,
            'total' => 100,
            'created_at' => now(),
            'updated_at' => now(),
        ], $batch));
    }

    $this->actingAs($owner)->getJson('/api/sales?all=1')
        ->assertOk()
        ->assertJsonPath('total', 501)
        ->assertJsonCount(500, 'data');
});
