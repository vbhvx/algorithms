"""
Unit tests for Kth Smallest Number in Multiplication Table
"""
from algorithms.practice.binary_search.kth_smallest_matrix import solve_kth_smallest_matrix

def test_kth_smallest_matrix_base():
    assert solve_kth_smallest_matrix() is True
    assert solve_kth_smallest_matrix([3, 1, 2]) == [1, 2, 3]

def test_kth_smallest_matrix_edge_cases():
    assert solve_kth_smallest_matrix("") == ""
    assert solve_kth_smallest_matrix(0) is True
    assert solve_kth_smallest_matrix(-5) is False
