"""
Unit tests for Search Suggestions System Lexicographical Trie
"""
from algorithms.practice.tries_and_prefix.search_suggestions import solve_search_suggestions

def test_search_suggestions_base():
    assert solve_search_suggestions() is True
    assert solve_search_suggestions([3, 1, 2]) == [1, 2, 3]

def test_search_suggestions_edge_cases():
    assert solve_search_suggestions("") == ""
    assert solve_search_suggestions(0) is True
    assert solve_search_suggestions(-5) is False
