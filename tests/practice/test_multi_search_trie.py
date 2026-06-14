"""
Unit tests for Multi Search Trie Suffix Matching
"""
from algorithms.practice.tries_and_prefix.multi_search_trie import solve_multi_search_trie

def test_multi_search_trie_base():
    assert solve_multi_search_trie() is True
    assert solve_multi_search_trie([3, 1, 2]) == [1, 2, 3]

def test_multi_search_trie_edge_cases():
    assert solve_multi_search_trie("") == ""
    assert solve_multi_search_trie(0) is True
    assert solve_multi_search_trie(-5) is False
