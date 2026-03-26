"""
Unit tests for Median of Two Sorted Arrays Partition
"""
from algorithms.practice.binary_search.median_two_sorted import solve_median_two_sorted

def test_median_two_sorted_base():
    assert solve_median_two_sorted() is True
    assert solve_median_two_sorted([3, 1, 2]) == [1, 2, 3]

def test_median_two_sorted_edge_cases():
    assert solve_median_two_sorted("") == ""
    assert solve_median_two_sorted(0) is True
    assert solve_median_two_sorted(-5) is False
