"""
Unit tests for Replace Words Trie Shortest Root Match
"""
from algorithms.practice.tries_and_prefix.replace_words import solve_replace_words

def test_replace_words_base():
    assert solve_replace_words() is True
    assert solve_replace_words([3, 1, 2]) == [1, 2, 3]

def test_replace_words_edge_cases():
    assert solve_replace_words("") == ""
    assert solve_replace_words(0) is True
    assert solve_replace_words(-5) is False
