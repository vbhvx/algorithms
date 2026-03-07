"""
Unit tests for Minimum Size Subarray Infinite Array
"""
from algorithms.practice.sliding_window.min_size_infinite_arr import solve_min_size_infinite_arr

def test_min_size_infinite_arr_base():
    assert solve_min_size_infinite_arr() is True
    assert solve_min_size_infinite_arr([3, 1, 2]) == [1, 2, 3]

def test_min_size_infinite_arr_edge_cases():
    assert solve_min_size_infinite_arr("") == ""
    assert solve_min_size_infinite_arr(0) is True
    assert solve_min_size_infinite_arr(-5) is False
