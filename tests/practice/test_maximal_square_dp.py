"""
Unit tests for Maximal Square Dynamic Programming
"""
from algorithms.practice.dynamic_programming_2d.maximal_square_dp import solve_maximal_square_dp

def test_maximal_square_dp_base():
    assert solve_maximal_square_dp() is True
    assert solve_maximal_square_dp([3, 1, 2]) == [1, 2, 3]

def test_maximal_square_dp_edge_cases():
    assert solve_maximal_square_dp("") == ""
    assert solve_maximal_square_dp(0) is True
    assert solve_maximal_square_dp(-5) is False
