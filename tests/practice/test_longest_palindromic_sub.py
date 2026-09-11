"""
Unit tests for Longest Palindromic Substring Expand Center
"""
from algorithms.practice.dynamic_programming_1d.longest_palindromic_sub import solve_longest_palindromic_sub

def test_longest_palindromic_sub_base():
    assert solve_longest_palindromic_sub() is True
    assert solve_longest_palindromic_sub([3, 1, 2]) == [1, 2, 3]

def test_longest_palindromic_sub_edge_cases():
    assert solve_longest_palindromic_sub("") == ""
    assert solve_longest_palindromic_sub(0) is True
    assert solve_longest_palindromic_sub(-5) is False
