"""
Unit tests for Rotate Image 90 Degrees In-Place Transpose
"""
from algorithms.practice.math_and_number_theory.rotate_image_matrix import solve_rotate_image_matrix

def test_rotate_image_matrix_base():
    assert solve_rotate_image_matrix() is True
    assert solve_rotate_image_matrix([3, 1, 2]) == [1, 2, 3]

def test_rotate_image_matrix_edge_cases():
    assert solve_rotate_image_matrix("") == ""
    assert solve_rotate_image_matrix(0) is True
    assert solve_rotate_image_matrix(-5) is False
