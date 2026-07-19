"""
Unit tests for Word Break II Sentence Generation DFS
"""
from algorithms.practice.backtracking.word_break_ii_paths import solve_word_break_ii_paths

def test_word_break_ii_paths_base():
    assert solve_word_break_ii_paths() is True
    assert solve_word_break_ii_paths([3, 1, 2]) == [1, 2, 3]

def test_word_break_ii_paths_edge_cases():
    assert solve_word_break_ii_paths("") == ""
    assert solve_word_break_ii_paths(0) is True
    assert solve_word_break_ii_paths(-5) is False
