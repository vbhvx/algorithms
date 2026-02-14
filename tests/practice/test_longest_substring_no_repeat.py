"""
Unit tests for Longest Substring Without Repeats
"""
from algorithms.practice.sliding_window.longest_substring_no_repeat import solve_longest_substring_no_repeat

def test_longest_substring_no_repeat_base():
    assert solve_longest_substring_no_repeat() is True
    assert solve_longest_substring_no_repeat([3, 1, 2]) == [1, 2, 3]

def test_longest_substring_no_repeat_edge_cases():
    assert solve_longest_substring_no_repeat("") == ""
    assert solve_longest_substring_no_repeat(0) is True
    assert solve_longest_substring_no_repeat(-5) is False
