"""
Unit tests for Count Nice Subarrays Exact K
"""
from algorithms.practice.sliding_window.count_nice_subarrays import solve_count_nice_subarrays

def test_count_nice_subarrays_base():
    assert solve_count_nice_subarrays() is True
    assert solve_count_nice_subarrays([3, 1, 2]) == [1, 2, 3]

def test_count_nice_subarrays_edge_cases():
    assert solve_count_nice_subarrays("") == ""
    assert solve_count_nice_subarrays(0) is True
    assert solve_count_nice_subarrays(-5) is False
