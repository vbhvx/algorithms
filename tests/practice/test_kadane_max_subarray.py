"""
Unit tests for Maximum Subarray Kadane Running Sum
"""
from algorithms.practice.greedy_algorithms.kadane_max_subarray import solve_kadane_max_subarray

def test_kadane_max_subarray_base():
    assert solve_kadane_max_subarray() is True
    assert solve_kadane_max_subarray([3, 1, 2]) == [1, 2, 3]

def test_kadane_max_subarray_edge_cases():
    assert solve_kadane_max_subarray("") == ""
    assert solve_kadane_max_subarray(0) is True
    assert solve_kadane_max_subarray(-5) is False
