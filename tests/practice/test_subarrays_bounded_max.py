"""
Unit tests for Subarrays with Bounded Maximum
"""
from algorithms.practice.sliding_window.subarrays_bounded_max import solve_subarrays_bounded_max

def test_subarrays_bounded_max_base():
    assert solve_subarrays_bounded_max() is True
    assert solve_subarrays_bounded_max([3, 1, 2]) == [1, 2, 3]

def test_subarrays_bounded_max_edge_cases():
    assert solve_subarrays_bounded_max("") == ""
    assert solve_subarrays_bounded_max(0) is True
    assert solve_subarrays_bounded_max(-5) is False
