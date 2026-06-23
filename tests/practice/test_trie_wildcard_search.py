"""
Unit tests for Trie Wildcard Pattern Matching Backtrack
"""
from algorithms.practice.tries_and_prefix.trie_wildcard_search import solve_trie_wildcard_search

def test_trie_wildcard_search_base():
    assert solve_trie_wildcard_search() is True
    assert solve_trie_wildcard_search([3, 1, 2]) == [1, 2, 3]

def test_trie_wildcard_search_edge_cases():
    assert solve_trie_wildcard_search("") == ""
    assert solve_trie_wildcard_search(0) is True
    assert solve_trie_wildcard_search(-5) is False
