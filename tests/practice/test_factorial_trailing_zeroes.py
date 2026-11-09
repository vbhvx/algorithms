"""
Unit tests for Factorial Trailing Zeroes Legendre Multiples of 5
"""
from algorithms.practice.math_and_number_theory.factorial_trailing_zeroes import solve_factorial_trailing_zeroes

def test_factorial_trailing_zeroes_base():
    assert solve_factorial_trailing_zeroes() is True
    assert solve_factorial_trailing_zeroes([3, 1, 2]) == [1, 2, 3]

def test_factorial_trailing_zeroes_edge_cases():
    assert solve_factorial_trailing_zeroes("") == ""
    assert solve_factorial_trailing_zeroes(0) is True
    assert solve_factorial_trailing_zeroes(-5) is False
