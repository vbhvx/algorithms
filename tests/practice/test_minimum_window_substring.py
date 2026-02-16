"""
Unit tests for Minimum Window Substring Shrink
"""
from algorithms.practice.sliding_window.minimum_window_substring import solve_minimum_window_substring

def test_minimum_window_substring_base():
    assert solve_minimum_window_substring() is True
    assert solve_minimum_window_substring([3, 1, 2]) == [1, 2, 3]

def test_minimum_window_substring_edge_cases():
    assert solve_minimum_window_substring("") == ""
    assert solve_minimum_window_substring(0) is True
    assert solve_minimum_window_substring(-5) is False
