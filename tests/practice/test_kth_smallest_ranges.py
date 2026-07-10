"""
Unit tests for Find Kth Smallest Element in Sorted Ranges
"""
from algorithms.practice.heaps_and_priority.kth_smallest_ranges import solve_kth_smallest_ranges

def test_kth_smallest_ranges_base():
    assert solve_kth_smallest_ranges() is True
    assert solve_kth_smallest_ranges([3, 1, 2]) == [1, 2, 3]

def test_kth_smallest_ranges_edge_cases():
    assert solve_kth_smallest_ranges("") == ""
    assert solve_kth_smallest_ranges(0) is True
    assert solve_kth_smallest_ranges(-5) is False
