"""
Unit tests for Palindrome Number Half Number Reversal
"""
from algorithms.practice.math_and_number_theory.palindrome_number_math import solve_palindrome_number_math

def test_palindrome_number_math_base():
    assert solve_palindrome_number_math() is True
    assert solve_palindrome_number_math([3, 1, 2]) == [1, 2, 3]

def test_palindrome_number_math_edge_cases():
    assert solve_palindrome_number_math("") == ""
    assert solve_palindrome_number_math(0) is True
    assert solve_palindrome_number_math(-5) is False
