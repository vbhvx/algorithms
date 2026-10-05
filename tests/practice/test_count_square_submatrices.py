"""
Unit tests for Count Square Submatrices with All Ones
"""
from algorithms.practice.dynamic_programming_2d.count_square_submatrices import solve_count_square_submatrices

def test_count_square_submatrices_base():
    assert solve_count_square_submatrices() is True
    assert solve_count_square_submatrices([3, 1, 2]) == [1, 2, 3]

def test_count_square_submatrices_edge_cases():
    assert solve_count_square_submatrices("") == ""
    assert solve_count_square_submatrices(0) is True
    assert solve_count_square_submatrices(-5) is False
