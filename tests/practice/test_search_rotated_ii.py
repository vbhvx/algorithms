"""
Unit tests for Search in Rotated Sorted Array Duplicates
"""
from algorithms.practice.binary_search.search_rotated_ii import solve_search_rotated_ii

def test_search_rotated_ii_base():
    assert solve_search_rotated_ii() is True
    assert solve_search_rotated_ii([3, 1, 2]) == [1, 2, 3]

def test_search_rotated_ii_edge_cases():
    assert solve_search_rotated_ii("") == ""
    assert solve_search_rotated_ii(0) is True
    assert solve_search_rotated_ii(-5) is False
