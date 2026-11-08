"""
Unit tests for Spiral Matrix II Layered Value Generation
"""
from algorithms.practice.math_and_number_theory.spiral_matrix_ii_gen import solve_spiral_matrix_ii_gen

def test_spiral_matrix_ii_gen_base():
    assert solve_spiral_matrix_ii_gen() is True
    assert solve_spiral_matrix_ii_gen([3, 1, 2]) == [1, 2, 3]

def test_spiral_matrix_ii_gen_edge_cases():
    assert solve_spiral_matrix_ii_gen("") == ""
    assert solve_spiral_matrix_ii_gen(0) is True
    assert solve_spiral_matrix_ii_gen(-5) is False
