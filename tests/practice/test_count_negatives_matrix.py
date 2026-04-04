"""
Unit tests for Count Negative Numbers in Sorted Matrix
"""
from algorithms.practice.binary_search.count_negatives_matrix import solve_count_negatives_matrix

def test_count_negatives_matrix_base():
    assert solve_count_negatives_matrix() is True
    assert solve_count_negatives_matrix([3, 1, 2]) == [1, 2, 3]

def test_count_negatives_matrix_edge_cases():
    assert solve_count_negatives_matrix("") == ""
    assert solve_count_negatives_matrix(0) is True
    assert solve_count_negatives_matrix(-5) is False
