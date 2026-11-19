<?php

namespace App\Http\Controllers;

use App\Models\Sale;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class DashboardController extends Controller
{
    public function index(Request $request)
    {
        $validated = $request->validate([
            'period' => 'sometimes|in:7d,30d',
            'branch_id' => 'sometimes|nullable|integer|exists:branches,id',
        ]);

        $branchId = $validated['branch_id'] ?? null;
        $days = ($validated['period'] ?? '7d') === '30d' ? 30 : 7;
        $today = now()->startOfDay();
        $from = $today->copy()->subDays($days - 1);
        $tomorrow = $today->copy()->addDay();
        $sales = Sale::query();

        if ($request->user()->role === 'cashier') {
            $sales->where('user_id', $request->user()->id);
        }

        if ($branchId) {
            $sales->where('branch_id', $branchId);
        }

        $sales->where('created_at', '>=', $from)
            ->where('created_at', '<', $tomorrow);

        $todaySummary = (clone $sales)->where('created_at', '>=', $today)
            ->selectRaw('COUNT(*) as count, COALESCE(SUM(total), 0) as revenue, COALESCE(AVG(total), 0) as average')
            ->first();

        $dailySales = (clone $sales)
            ->selectRaw('DATE(created_at) as day, COUNT(*) as count, COALESCE(SUM(total), 0) as revenue')
            ->groupByRaw('DATE(created_at)')
            ->orderBy('day')
            ->get();

        $topProducts = DB::table('sale_items')
            ->join('sales', 'sales.id', '=', 'sale_items.sale_id')
            ->leftJoin('products', 'products.id', '=', 'sale_items.product_id')
            ->when($request->user()->role === 'cashier', fn ($query) => $query->where('sales.user_id', $request->user()->id))
            ->when($branchId, fn ($query) => $query->where('sales.branch_id', $branchId))
            ->where('sales.created_at', '>=', $from)
            ->where('sales.created_at', '<', $tomorrow)
            ->select('sale_items.product_id', 'products.name', 'products.sku')
            ->selectRaw('SUM(sale_items.quantity) as units, SUM(sale_items.line_total) as revenue')
            ->groupBy('sale_items.product_id', 'products.name', 'products.sku')
            ->orderByDesc('revenue')
            ->limit(5)
            ->get();

        $recentSales = (clone $sales)->with('user:id,name')
            ->latest()
            ->limit(6)
            ->get(['id', 'user_id', 'total', 'payment_method', 'created_at']);

        $lowStock = DB::table('products')
            ->join('inventories', 'inventories.product_id', '=', 'products.id')
            ->where('products.is_active', true)
            ->when($branchId, fn ($query) => $query->where('products.branch_id', $branchId))
            ->whereColumn('inventories.quantity', '<=', 'inventories.reorder_threshold')
            ->orderBy('inventories.quantity')
            ->get([
                'products.id', 'products.name',
                'inventories.quantity', 'inventories.reorder_threshold',
            ]);

        return response()->json([
            'today' => [
                'count' => (int) $todaySummary->count,
                'revenue' => (float) $todaySummary->revenue,
                'average' => round((float) $todaySummary->average, 2),
            ],
            'period' => [
                'days' => $days,
                'from' => $from->toDateString(),
                'to' => $today->toDateString(),
            ],
            'daily_sales' => $dailySales,
            'top_products' => $topProducts,
            'recent_sales' => $recentSales,
            'low_stock' => $lowStock,
        ]);
    }
}
