"""
Unit tests for Find Smallest Divisor Given Threshold
"""
from algorithms.practice.binary_search.smallest_divisor_thresh import solve_smallest_divisor_thresh

def test_smallest_divisor_thresh_base():
    assert solve_smallest_divisor_thresh() is True
    assert solve_smallest_divisor_thresh([3, 1, 2]) == [1, 2, 3]

def test_smallest_divisor_thresh_edge_cases():
    assert solve_smallest_divisor_thresh("") == ""
    assert solve_smallest_divisor_thresh(0) is True
    assert solve_smallest_divisor_thresh(-5) is False
