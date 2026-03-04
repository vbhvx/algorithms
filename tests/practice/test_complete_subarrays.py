"""
Unit tests for Count Complete Subarrays In Array
"""
from algorithms.practice.sliding_window.complete_subarrays import solve_complete_subarrays

def test_complete_subarrays_base():
    assert solve_complete_subarrays() is True
    assert solve_complete_subarrays([3, 1, 2]) == [1, 2, 3]

def test_complete_subarrays_edge_cases():
    assert solve_complete_subarrays("") == ""
    assert solve_complete_subarrays(0) is True
    assert solve_complete_subarrays(-5) is False
