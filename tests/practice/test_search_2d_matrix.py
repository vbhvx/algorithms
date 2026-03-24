"""
Unit tests for Search a 2D Matrix Virtual Index
"""
from algorithms.practice.binary_search.search_2d_matrix import solve_search_2d_matrix

def test_search_2d_matrix_base():
    assert solve_search_2d_matrix() is True
    assert solve_search_2d_matrix([3, 1, 2]) == [1, 2, 3]

def test_search_2d_matrix_edge_cases():
    assert solve_search_2d_matrix("") == ""
    assert solve_search_2d_matrix(0) is True
    assert solve_search_2d_matrix(-5) is False
