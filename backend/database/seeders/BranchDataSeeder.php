<?php

namespace Database\Seeders;

use App\Models\Branch;
use App\Models\Product;
use App\Models\Sale;
use App\Models\StockAdjustment;
use App\Models\User;
use Illuminate\Database\Seeder;

class BranchDataSeeder extends Seeder
{
    public function run(): void
    {
        $branchDefs = [
            [
                'code' => 'BR-001',
                'name' => 'Victoria Island Main Branch',
                'address' => 'Plot 5, Commercial Block West, Victoria Island, Lagos',
                'phone' => '+234 1 270 0000',
                'is_active' => true,
            ],
            [
                'code' => 'BR-002',
                'name' => 'Ikeja Annex Branch',
                'address' => '42 Allen Avenue, Ikeja, Lagos',
                'phone' => '+234 1 270 0001',
                'is_active' => true,
            ],
            [
                'code' => 'BR-003',
                'name' => 'Lekki Phase 1 Store',
                'address' => '15 Admiralty Way, Lekki Phase 1, Lagos',
                'phone' => '+234 1 270 0002',
                'is_active' => true,
            ],
            [
                'code' => 'BR-004',
                'name' => 'Abuja Wuse II Hub',
                'address' => '88 Aminu Kano Crescent, Wuse II, Abuja',
                'phone' => '+234 9 461 0003',
                'is_active' => true,
            ],
        ];

        $branches = [];
        foreach ($branchDefs as $def) {
            $branches[$def['code']] = Branch::updateOrCreate(
                ['code' => $def['code']],
                $def
            );
        }

        // Assign existing staff to branches & seed branch cashiers
        User::where('email', 'owner@example.com')->update(['branch_id' => $branches['BR-001']->id]);
        User::where('email', 'manager@example.com')->update(['branch_id' => $branches['BR-001']->id]);
        User::where('email', 'amina@cwgretail.com')->update(['branch_id' => $branches['BR-001']->id]);
        User::where('email', 'tunde@cwgretail.com')->update(['branch_id' => $branches['BR-002']->id]);
        User::where('email', 'cashier@example.com')->update(['branch_id' => $branches['BR-002']->id]);

        $lekkiCashier = User::updateOrCreate(
            ['email' => 'chiamaka@cwgretail.com'],
            [
                'branch_id' => $branches['BR-003']->id,
                'name' => 'Chiamaka Nwosu',
                'password' => 'password',
                'role' => 'cashier',
                'status' => 'active',
            ]
        );

        $abujaCashier = User::updateOrCreate(
            ['email' => 'musa@cwgretail.com'],
            [
                'branch_id' => $branches['BR-004']->id,
                'name' => 'Musa Abdullahi',
                'password' => 'password',
                'role' => 'cashier',
                'status' => 'active',
            ]
        );

        $tunde = User::where('email', 'tunde@cwgretail.com')->first() ?? User::first();
        $amina = User::where('email', 'amina@cwgretail.com')->first() ?? User::first();

        $catalogTemplates = [
            ['Nestlé Milo Energy Food Drink 500g', 'NES-MILO-500', 'beverages', 'tin', 3400, 4200, '/storage/products/nes-milo-500.jpg', 48, 12],
            ['Dano Full Cream Milk Powder 800g', 'DAN-MLK-800', 'beverages', 'pack', 4300, 5400, '/storage/products/dan-mlk-800.jpg', 32, 10],
            ['Indomie Instant Noodles Onion Chicken (Ctn)', 'IND-ONC-CTN', 'grains_staples', 'carton', 8100, 9800, '/storage/products/ind-onc-ctn.jpg', 30, 8],
            ['Coca-Cola Original Taste 50cl PET', 'COK-50-PET', 'beverages', 'bottle', 380, 500, '/storage/products/cok-50-pet.jpg', 120, 24],
            ['Peak Evaporated Milk Tin 160g', 'PEK-EVAP-160', 'beverages', 'tin', 510, 650, '/storage/products/pek-evap-160.jpg', 96, 20],
            ['Mama Gold Thai Parboiled Rice 50kg', 'MAM-RIC-50K', 'grains_staples', 'bag', 69000, 78500, '/storage/products/mam-ric-50k.jpg', 14, 5],
            ["Devon King's Pure Cooking Oil 5L", 'DEV-OIL-5L', 'cooking_oils', 'bottle', 14500, 17200, '/storage/products/dev-oil-5l.jpg', 18, 6],
            ['Sunlight 2in1 Detergent 900g', 'SUN-DET-900', 'household_cleaning', 'pack', 1950, 2500, '/storage/products/sun-det-900.jpg', 40, 10],
            ['Dettol Antiseptic Liquid 500ml', 'DET-ANT-500', 'personal_care', 'bottle', 2700, 3300, '/storage/products/det-ant-500.jpg', 28, 8],
        ];

        $branchConfigs = [
            'BR-002' => ['suffix' => 'IKJ', 'cashier' => $tunde, 'stockMult' => 0.8, 'salesCount' => 6],
            'BR-003' => ['suffix' => 'LEK', 'cashier' => $lekkiCashier, 'stockMult' => 1.1, 'salesCount' => 5],
            'BR-004' => ['suffix' => 'ABJ', 'cashier' => $abujaCashier, 'stockMult' => 0.6, 'salesCount' => 4],
        ];

        foreach ($branchConfigs as $code => $cfg) {
            $branch = $branches[$code];
            $branchProducts = [];

            foreach ($catalogTemplates as $idx => $tpl) {
                $sku = $tpl[1] . '-' . $cfg['suffix'];
                $product = Product::firstOrCreate(
                    ['sku' => $sku],
                    [
                        'branch_id' => $branch->id,
                        'name' => $tpl[0],
                        'category' => $tpl[2],
                        'unit' => $tpl[3],
                        'cost_price' => $tpl[4],
                        'sell_price' => $tpl[5],
                        'image_path' => $tpl[6],
                        'is_active' => true,
                    ]
                );

                if (! $product->inventory) {
                    $qty = max(3, (int) round($tpl[7] * $cfg['stockMult']) - ($idx === 5 ? 9 : 0));
                    $product->inventory()->create([
                        'quantity' => $qty,
                        'reorder_threshold' => $tpl[8],
                    ]);
                }

                $branchProducts[] = $product;
            }

            // Only seed sales for this branch if none exist yet
            if (Sale::where('branch_id', $branch->id)->count() === 0 && count($branchProducts) > 0) {
                $methods = ['cash', 'card', 'bank_transfer'];
                for ($i = 0; $i < $cfg['salesCount']; $i++) {
                    $p1 = $branchProducts[$i % count($branchProducts)];
                    $p2 = $branchProducts[($i + 2) % count($branchProducts)];
                    $q1 = ($i % 3) + 1;
                    $q2 = ($i % 2) + 1;
                    $l1 = round((float) $p1->sell_price * $q1, 2);
                    $l2 = round((float) $p2->sell_price * $q2, 2);
                    $total = round($l1 + $l2, 2);

                    $sale = Sale::create([
                        'branch_id' => $branch->id,
                        'user_id' => $cfg['cashier']->id,
                        'payment_method' => $methods[$i % 3],
                        'subtotal' => $total,
                        'total' => $total,
                        'created_at' => now()->subDays($i)->setTime(10 + $i, 15),
                        'updated_at' => now()->subDays($i)->setTime(10 + $i, 15),
                    ]);

                    $sale->items()->createMany([
                        ['product_id' => $p1->id, 'quantity' => $q1, 'unit_price' => $p1->sell_price, 'line_total' => $l1],
                        ['product_id' => $p2->id, 'quantity' => $q2, 'unit_price' => $p2->sell_price, 'line_total' => $l2],
                    ]);
                }

                // Seed 2 stock adjustments per branch
                StockAdjustment::create([
                    'branch_id' => $branch->id,
                    'product_id' => $branchProducts[0]->id,
                    'user_id' => $cfg['cashier']->id,
                    'type' => 'increase',
                    'quantity_change' => 20,
                    'reason' => "Initial branch opening stock intake ({$code})",
                ]);
            }
        }

        // Also seed 3 recent sales on BR-001 so its 7-day dashboard/report charts are active
        $br1Products = Product::where('branch_id', $branches['BR-001']->id)->take(5)->get();
        if ($br1Products->count() >= 2 && Sale::where('branch_id', $branches['BR-001']->id)->where('created_at', '>=', now()->subDays(6))->count() === 0) {
            foreach ([0, 1, 2] as $d) {
                $p = $br1Products[$d];
                $line = round((float) $p->sell_price * 2, 2);
                $s = Sale::create([
                    'branch_id' => $branches['BR-001']->id,
                    'user_id' => $amina->id,
                    'payment_method' => $d === 0 ? 'card' : 'cash',
                    'subtotal' => $line,
                    'total' => $line,
                    'created_at' => now()->subDays($d)->setTime(11 + $d, 30),
                    'updated_at' => now()->subDays($d)->setTime(11 + $d, 30),
                ]);
                $s->items()->create([
                    'product_id' => $p->id,
                    'quantity' => 2,
                    'unit_price' => $p->sell_price,
                    'line_total' => $line,
                ]);
            }
        }
    }
}
