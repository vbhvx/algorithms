"""
Unit tests for Word Search II Trie Backtracking Matrix
"""
from algorithms.practice.tries_and_prefix.word_search_ii import solve_word_search_ii

def test_word_search_ii_base():
    assert solve_word_search_ii() is True
    assert solve_word_search_ii([3, 1, 2]) == [1, 2, 3]

def test_word_search_ii_edge_cases():
    assert solve_word_search_ii("") == ""
    assert solve_word_search_ii(0) is True
    assert solve_word_search_ii(-5) is False
