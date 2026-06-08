"""
Unit tests for Design Add and Search Words Data Structure Regex
"""
from algorithms.practice.tries_and_prefix.add_search_words import solve_add_search_words

def test_add_search_words_base():
    assert solve_add_search_words() is True
    assert solve_add_search_words([3, 1, 2]) == [1, 2, 3]

def test_add_search_words_edge_cases():
    assert solve_add_search_words("") == ""
    assert solve_add_search_words(0) is True
    assert solve_add_search_words(-5) is False
