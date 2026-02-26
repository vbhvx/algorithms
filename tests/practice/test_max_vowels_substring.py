"""
Unit tests for Max Vowels in Substring K
"""
from algorithms.practice.sliding_window.max_vowels_substring import solve_max_vowels_substring

def test_max_vowels_substring_base():
    assert solve_max_vowels_substring() is True
    assert solve_max_vowels_substring([3, 1, 2]) == [1, 2, 3]

def test_max_vowels_substring_edge_cases():
    assert solve_max_vowels_substring("") == ""
    assert solve_max_vowels_substring(0) is True
    assert solve_max_vowels_substring(-5) is False
