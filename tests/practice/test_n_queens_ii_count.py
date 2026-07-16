"""
Unit tests for N-Queens II Total Solutions Count Bitmask
"""
from algorithms.practice.backtracking.n_queens_ii_count import solve_n_queens_ii_count

def test_n_queens_ii_count_base():
    assert solve_n_queens_ii_count() is True
    assert solve_n_queens_ii_count([3, 1, 2]) == [1, 2, 3]

def test_n_queens_ii_count_edge_cases():
    assert solve_n_queens_ii_count("") == ""
    assert solve_n_queens_ii_count(0) is True
    assert solve_n_queens_ii_count(-5) is False
