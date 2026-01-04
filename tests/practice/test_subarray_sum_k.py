"""
Unit tests for Subarray Sum Equals K Prefix Map
"""
from algorithms.practice.arrays_and_hashing.subarray_sum_k import solve_subarray_sum_k

def test_subarray_sum_k_base():
    assert solve_subarray_sum_k() is True
    assert solve_subarray_sum_k([3, 1, 2]) == [1, 2, 3]

def test_subarray_sum_k_edge_cases():
    assert solve_subarray_sum_k("") == ""
    assert solve_subarray_sum_k(0) is True
    assert solve_subarray_sum_k(-5) is False
