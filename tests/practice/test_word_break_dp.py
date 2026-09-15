"""
Unit tests for Word Break Prefix Verification Set
"""
from algorithms.practice.dynamic_programming_1d.word_break_dp import solve_word_break_dp

def test_word_break_dp_base():
    assert solve_word_break_dp() is True
    assert solve_word_break_dp([3, 1, 2]) == [1, 2, 3]

def test_word_break_dp_edge_cases():
    assert solve_word_break_dp("") == ""
    assert solve_word_break_dp(0) is True
    assert solve_word_break_dp(-5) is False
