"""
Unit tests for Find Minimum Rotated Sorted Array Duplicates
"""
from algorithms.practice.binary_search.find_min_rotated_ii import solve_find_min_rotated_ii

def test_find_min_rotated_ii_base():
    assert solve_find_min_rotated_ii() is True
    assert solve_find_min_rotated_ii([3, 1, 2]) == [1, 2, 3]

def test_find_min_rotated_ii_edge_cases():
    assert solve_find_min_rotated_ii("") == ""
    assert solve_find_min_rotated_ii(0) is True
    assert solve_find_min_rotated_ii(-5) is False
