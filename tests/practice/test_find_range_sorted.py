"""
Unit tests for Find First and Last Position in Sorted Array
"""
from algorithms.practice.binary_search.find_range_sorted import solve_find_range_sorted

def test_find_range_sorted_base():
    assert solve_find_range_sorted() is True
    assert solve_find_range_sorted([3, 1, 2]) == [1, 2, 3]

def test_find_range_sorted_edge_cases():
    assert solve_find_range_sorted("") == ""
    assert solve_find_range_sorted(0) is True
    assert solve_find_range_sorted(-5) is False
