"""
Unit tests for Multiply Strings Large Arithmetic Manual Carry
"""
from algorithms.practice.math_and_number_theory.multiply_strings_large import solve_multiply_strings_large

def test_multiply_strings_large_base():
    assert solve_multiply_strings_large() is True
    assert solve_multiply_strings_large([3, 1, 2]) == [1, 2, 3]

def test_multiply_strings_large_edge_cases():
    assert solve_multiply_strings_large("") == ""
    assert solve_multiply_strings_large(0) is True
    assert solve_multiply_strings_large(-5) is False
