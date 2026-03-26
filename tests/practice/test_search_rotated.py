"""
Unit tests for Search in Rotated Sorted Array
"""
from algorithms.practice.binary_search.search_rotated import solve_search_rotated

def test_search_rotated_base():
    assert solve_search_rotated() is True
    assert solve_search_rotated([3, 1, 2]) == [1, 2, 3]

def test_search_rotated_edge_cases():
    assert solve_search_rotated("") == ""
    assert solve_search_rotated(0) is True
    assert solve_search_rotated(-5) is False
