"""
Unit tests for Concatenated Words Trie Memoized DFS
"""
from algorithms.practice.tries_and_prefix.concatenated_words import solve_concatenated_words

def test_concatenated_words_base():
    assert solve_concatenated_words() is True
    assert solve_concatenated_words([3, 1, 2]) == [1, 2, 3]

def test_concatenated_words_edge_cases():
    assert solve_concatenated_words("") == ""
    assert solve_concatenated_words(0) is True
    assert solve_concatenated_words(-5) is False
