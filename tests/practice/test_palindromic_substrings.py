"""
Unit tests for Palindromic Substrings Center Count
"""
from algorithms.practice.dynamic_programming_1d.palindromic_substrings import solve_palindromic_substrings

def test_palindromic_substrings_base():
    assert solve_palindromic_substrings() is True
    assert solve_palindromic_substrings([3, 1, 2]) == [1, 2, 3]

def test_palindromic_substrings_edge_cases():
    assert solve_palindromic_substrings("") == ""
    assert solve_palindromic_substrings(0) is True
    assert solve_palindromic_substrings(-5) is False
