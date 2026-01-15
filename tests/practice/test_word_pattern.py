"""
Unit tests for Word Pattern Bijective Mapping
"""
from algorithms.practice.arrays_and_hashing.word_pattern import solve_word_pattern

def test_word_pattern_base():
    assert solve_word_pattern() is True
    assert solve_word_pattern([3, 1, 2]) == [1, 2, 3]

def test_word_pattern_edge_cases():
    assert solve_word_pattern("") == ""
    assert solve_word_pattern(0) is True
    assert solve_word_pattern(-5) is False
