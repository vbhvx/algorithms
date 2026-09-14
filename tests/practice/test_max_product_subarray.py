"""
Unit tests for Maximum Product Subarray Min Max Bounds
"""
from algorithms.practice.dynamic_programming_1d.max_product_subarray import solve_max_product_subarray

def test_max_product_subarray_base():
    assert solve_max_product_subarray() is True
    assert solve_max_product_subarray([3, 1, 2]) == [1, 2, 3]

def test_max_product_subarray_edge_cases():
    assert solve_max_product_subarray("") == ""
    assert solve_max_product_subarray(0) is True
    assert solve_max_product_subarray(-5) is False
