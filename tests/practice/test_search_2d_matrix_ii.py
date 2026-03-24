"""
Unit tests for Search a 2D Matrix II Top Right Step
"""
from algorithms.practice.binary_search.search_2d_matrix_ii import solve_search_2d_matrix_ii

def test_search_2d_matrix_ii_base():
    assert solve_search_2d_matrix_ii() is True
    assert solve_search_2d_matrix_ii([3, 1, 2]) == [1, 2, 3]

def test_search_2d_matrix_ii_edge_cases():
    assert solve_search_2d_matrix_ii("") == ""
    assert solve_search_2d_matrix_ii(0) is True
    assert solve_search_2d_matrix_ii(-5) is False
