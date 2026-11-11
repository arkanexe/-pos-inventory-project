<?php

use App\Models\Inventory;
use App\Models\Product;
use App\Models\Sale;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;

uses(RefreshDatabase::class);

test('dashboard returns bounded aggregate data scoped to the cashier', function () {
    $cashier = User::factory()->create(['role' => 'cashier']);
    $otherCashier = User::factory()->create(['role' => 'cashier']);
    $owner = User::factory()->create(['role' => 'owner']);
    $product = Product::create([
        'name' => 'Soap',
        'sku' => 'SOAP-001',
        'category' => 'Household',
        'cost_price' => 100,
        'sell_price' => 150,
        'is_active' => true,
    ]);
    Inventory::create([
        'product_id' => $product->id,
        'quantity' => 1,
        'reorder_threshold' => 2,
    ]);

    foreach ([$cashier, $otherCashier] as $user) {
        $sale = Sale::create([
            'user_id' => $user->id,
            'payment_method' => 'cash',
            'subtotal' => 300,
            'total' => 300,
        ]);
        $sale->items()->create([
            'product_id' => $product->id,
            'quantity' => 2,
            'unit_price' => 150,
            'line_total' => 300,
        ]);
    }

    $olderSale = Sale::create([
        'user_id' => $cashier->id,
        'payment_method' => 'card',
        'subtotal' => 900,
        'total' => 900,
    ]);
    $olderSale->forceFill(['created_at' => now()->subDays(31), 'updated_at' => now()->subDays(31)])->save();

    $this->actingAs($cashier)->getJson('/api/dashboard?period=7d')
        ->assertOk()
        ->assertJsonPath('today.count', 1)
        ->assertJsonPath('top_products.0.units', 2)
        ->assertJsonCount(1, 'recent_sales')
        ->assertJsonPath('low_stock.0.name', 'Soap');

    $this->actingAs($owner)->getJson('/api/dashboard?period=7d')
        ->assertOk()
        ->assertJsonPath('today.count', 2)
        ->assertJsonPath('top_products.0.units', 4)
        ->assertJsonCount(2, 'recent_sales');
});

test('dashboard validates its period and requires authentication', function () {
    $this->getJson('/api/dashboard')->assertUnauthorized();

    $user = User::factory()->create(['role' => 'cashier']);
    $this->actingAs($user)->getJson('/api/dashboard?period=year')
        ->assertUnprocessable();
});
