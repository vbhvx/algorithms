"""
Unit tests for Set Matrix Zeroes First Row Column Marker
"""
from algorithms.practice.math_and_number_theory.set_matrix_zeroes import solve_set_matrix_zeroes

def test_set_matrix_zeroes_base():
    assert solve_set_matrix_zeroes() is True
    assert solve_set_matrix_zeroes([3, 1, 2]) == [1, 2, 3]

def test_set_matrix_zeroes_edge_cases():
    assert solve_set_matrix_zeroes("") == ""
    assert solve_set_matrix_zeroes(0) is True
    assert solve_set_matrix_zeroes(-5) is False
