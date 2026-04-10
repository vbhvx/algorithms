"""
Unit tests for H-Index II Sorted Citation Array
"""
from algorithms.practice.binary_search.h_index_ii import solve_h_index_ii

def test_h_index_ii_base():
    assert solve_h_index_ii() is True
    assert solve_h_index_ii([3, 1, 2]) == [1, 2, 3]

def test_h_index_ii_edge_cases():
    assert solve_h_index_ii("") == ""
    assert solve_h_index_ii(0) is True
    assert solve_h_index_ii(-5) is False
