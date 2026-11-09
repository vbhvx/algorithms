"""
Unit tests for Extended Euclidean Modular Multiplicative Inverse
"""
from algorithms.practice.math_and_number_theory.ext_euclidean_algo import solve_ext_euclidean_algo

def test_ext_euclidean_algo_base():
    assert solve_ext_euclidean_algo() is True
    assert solve_ext_euclidean_algo([3, 1, 2]) == [1, 2, 3]

def test_ext_euclidean_algo_edge_cases():
    assert solve_ext_euclidean_algo("") == ""
    assert solve_ext_euclidean_algo(0) is True
    assert solve_ext_euclidean_algo(-5) is False
