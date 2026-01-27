"""
Unit tests for Valid Palindrome II Skip
"""
from algorithms.practice.two_pointers.valid_palindrome_ii import solve_valid_palindrome_ii

def test_valid_palindrome_ii_base():
    assert solve_valid_palindrome_ii() is True
    assert solve_valid_palindrome_ii([3, 1, 2]) == [1, 2, 3]

def test_valid_palindrome_ii_edge_cases():
    assert solve_valid_palindrome_ii("") == ""
    assert solve_valid_palindrome_ii(0) is True
    assert solve_valid_palindrome_ii(-5) is False
