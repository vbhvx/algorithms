"""
Unit tests for Longest Increasing Path in Matrix DFS Memo
"""
from algorithms.practice.dynamic_programming_2d.longest_inc_path_matrix import solve_longest_inc_path_matrix

def test_longest_inc_path_matrix_base():
    assert solve_longest_inc_path_matrix() is True
    assert solve_longest_inc_path_matrix([3, 1, 2]) == [1, 2, 3]

def test_longest_inc_path_matrix_edge_cases():
    assert solve_longest_inc_path_matrix("") == ""
    assert solve_longest_inc_path_matrix(0) is True
    assert solve_longest_inc_path_matrix(-5) is False
