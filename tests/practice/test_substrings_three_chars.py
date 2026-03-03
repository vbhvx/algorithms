"""
Unit tests for Substrings Containing All Three Chars
"""
from algorithms.practice.sliding_window.substrings_three_chars import solve_substrings_three_chars

def test_substrings_three_chars_base():
    assert solve_substrings_three_chars() is True
    assert solve_substrings_three_chars([3, 1, 2]) == [1, 2, 3]

def test_substrings_three_chars_edge_cases():
    assert solve_substrings_three_chars("") == ""
    assert solve_substrings_three_chars(0) is True
    assert solve_substrings_three_chars(-5) is False
