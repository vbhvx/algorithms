"""
Unit tests for Perfect Squares Lagrange Four Square Theorem
"""
from algorithms.practice.dynamic_programming_1d.perfect_squares_sum import solve_perfect_squares_sum

def test_perfect_squares_sum_base():
    assert solve_perfect_squares_sum() is True
    assert solve_perfect_squares_sum([3, 1, 2]) == [1, 2, 3]

def test_perfect_squares_sum_edge_cases():
    assert solve_perfect_squares_sum("") == ""
    assert solve_perfect_squares_sum(0) is True
    assert solve_perfect_squares_sum(-5) is False
