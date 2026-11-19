<?php

namespace App\Http\Controllers;

use App\Models\Branch;
use Illuminate\Http\Request;

class BranchController extends Controller
{
    public function index(Request $request)
    {
        $query = Branch::withCount(['products', 'sales', 'users'])
            ->orderBy('id');

        if ($request->boolean('active')) {
            $query->where('is_active', true);
        }

        return response()->json($query->get());
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'code' => 'required|string|max:32|unique:branches,code',
            'address' => 'nullable|string|max:255',
            'phone' => 'nullable|string|max:40',
            'is_active' => 'sometimes|boolean',
        ]);

        $branch = Branch::create([
            'name' => trim($validated['name']),
            'code' => strtoupper(trim($validated['code'])),
            'address' => $validated['address'] ?? null,
            'phone' => $validated['phone'] ?? null,
            'is_active' => $validated['is_active'] ?? true,
        ]);

        return response()->json(
            $branch->loadCount(['products', 'sales', 'users']),
            201
        );
    }

    public function update(Request $request, Branch $branch)
    {
        $validated = $request->validate([
            'name' => 'sometimes|required|string|max:255',
            'code' => 'sometimes|required|string|max:32|unique:branches,code,' . $branch->id,
            'address' => 'nullable|string|max:255',
            'phone' => 'nullable|string|max:40',
            'is_active' => 'sometimes|boolean',
        ]);

        if (isset($validated['code'])) {
            $validated['code'] = strtoupper(trim($validated['code']));
        }

        $branch->update($validated);

        return response()->json(
            $branch->fresh()->loadCount(['products', 'sales', 'users'])
        );
    }

    public function destroy(Branch $branch)
    {
        if ($branch->sales()->exists() || $branch->products()->exists()) {
            return response()->json([
                'message' => 'Cannot delete a branch with existing products or sales. Deactivate it instead.',
            ], 422);
        }

        $branch->delete();

        return response()->json([
            'message' => 'Branch deleted successfully.',
        ]);
    }
}
