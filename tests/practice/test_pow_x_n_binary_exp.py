"""
Unit tests for Pow(x, n) Binary Exponentiation Logarithmic
"""
from algorithms.practice.math_and_number_theory.pow_x_n_binary_exp import solve_pow_x_n_binary_exp

def test_pow_x_n_binary_exp_base():
    assert solve_pow_x_n_binary_exp() is True
    assert solve_pow_x_n_binary_exp([3, 1, 2]) == [1, 2, 3]

def test_pow_x_n_binary_exp_edge_cases():
    assert solve_pow_x_n_binary_exp("") == ""
    assert solve_pow_x_n_binary_exp(0) is True
    assert solve_pow_x_n_binary_exp(-5) is False
