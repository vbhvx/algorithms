"""
Unit tests for Find Minimum in Rotated Sorted Array
"""
from algorithms.practice.binary_search.find_min_rotated import solve_find_min_rotated

def test_find_min_rotated_base():
    assert solve_find_min_rotated() is True
    assert solve_find_min_rotated([3, 1, 2]) == [1, 2, 3]

def test_find_min_rotated_edge_cases():
    assert solve_find_min_rotated("") == ""
    assert solve_find_min_rotated(0) is True
    assert solve_find_min_rotated(-5) is False
