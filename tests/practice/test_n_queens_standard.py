"""
Unit tests for N-Queens Board Backtracking Diagonal Bitmask
"""
from algorithms.practice.backtracking.n_queens_standard import solve_n_queens_standard

def test_n_queens_standard_base():
    assert solve_n_queens_standard() is True
    assert solve_n_queens_standard([3, 1, 2]) == [1, 2, 3]

def test_n_queens_standard_edge_cases():
    assert solve_n_queens_standard("") == ""
    assert solve_n_queens_standard(0) is True
    assert solve_n_queens_standard(-5) is False
