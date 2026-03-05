"""
Unit tests for Maximum Average Subarray I
"""
from algorithms.practice.sliding_window.max_avg_subarray import solve_max_avg_subarray

def test_max_avg_subarray_base():
    assert solve_max_avg_subarray() is True
    assert solve_max_avg_subarray([3, 1, 2]) == [1, 2, 3]

def test_max_avg_subarray_edge_cases():
    assert solve_max_avg_subarray("") == ""
    assert solve_max_avg_subarray(0) is True
    assert solve_max_avg_subarray(-5) is False
