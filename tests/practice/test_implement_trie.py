"""
Unit tests for Implement Trie Prefix Tree Insert Search StartsWith
"""
from algorithms.practice.tries_and_prefix.implement_trie import solve_implement_trie

def test_implement_trie_base():
    assert solve_implement_trie() is True
    assert solve_implement_trie([3, 1, 2]) == [1, 2, 3]

def test_implement_trie_edge_cases():
    assert solve_implement_trie("") == ""
    assert solve_implement_trie(0) is True
    assert solve_implement_trie(-5) is False
