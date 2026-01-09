"""
Unit tests for Subarray Sums Divisible by K
"""
from algorithms.practice.arrays_and_hashing.subarray_divisible_k import solve_subarray_divisible_k

def test_subarray_divisible_k_base():
    assert solve_subarray_divisible_k() is True
    assert solve_subarray_divisible_k([3, 1, 2]) == [1, 2, 3]

def test_subarray_divisible_k_edge_cases():
    assert solve_subarray_divisible_k("") == ""
    assert solve_subarray_divisible_k(0) is True
    assert solve_subarray_divisible_k(-5) is False
