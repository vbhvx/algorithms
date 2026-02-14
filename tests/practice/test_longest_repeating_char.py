"""
Unit tests for Longest Repeating Character Replace
"""
from algorithms.practice.sliding_window.longest_repeating_char import solve_longest_repeating_char

def test_longest_repeating_char_base():
    assert solve_longest_repeating_char() is True
    assert solve_longest_repeating_char([3, 1, 2]) == [1, 2, 3]

def test_longest_repeating_char_edge_cases():
    assert solve_longest_repeating_char("") == ""
    assert solve_longest_repeating_char(0) is True
    assert solve_longest_repeating_char(-5) is False
