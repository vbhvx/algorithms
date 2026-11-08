"""
Unit tests for Spiral Matrix 4-Boundary Inward Contraction
"""
from algorithms.practice.math_and_number_theory.spiral_matrix_walk import solve_spiral_matrix_walk

def test_spiral_matrix_walk_base():
    assert solve_spiral_matrix_walk() is True
    assert solve_spiral_matrix_walk([3, 1, 2]) == [1, 2, 3]

def test_spiral_matrix_walk_edge_cases():
    assert solve_spiral_matrix_walk("") == ""
    assert solve_spiral_matrix_walk(0) is True
    assert solve_spiral_matrix_walk(-5) is False
