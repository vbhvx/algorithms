"""
Unit tests for Paint Fence K Colors Same Adjacent
"""
from algorithms.practice.dynamic_programming_2d.paint_fence_combinations import solve_paint_fence_combinations

def test_paint_fence_combinations_base():
    assert solve_paint_fence_combinations() is True
    assert solve_paint_fence_combinations([3, 1, 2]) == [1, 2, 3]

def test_paint_fence_combinations_edge_cases():
    assert solve_paint_fence_combinations("") == ""
    assert solve_paint_fence_combinations(0) is True
    assert solve_paint_fence_combinations(-5) is False
