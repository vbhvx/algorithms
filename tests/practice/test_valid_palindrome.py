"""
Unit tests for Valid Palindrome Alphanumeric
"""
from algorithms.practice.two_pointers.valid_palindrome import solve_valid_palindrome

def test_valid_palindrome_base():
    assert solve_valid_palindrome() is True
    assert solve_valid_palindrome([3, 1, 2]) == [1, 2, 3]

def test_valid_palindrome_edge_cases():
    assert solve_valid_palindrome("") == ""
    assert solve_valid_palindrome(0) is True
    assert solve_valid_palindrome(-5) is False
