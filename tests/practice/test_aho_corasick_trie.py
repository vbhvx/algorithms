"""
Unit tests for Aho Corasick Trie Dictionary Matching
"""
from algorithms.practice.tries_and_prefix.aho_corasick_trie import solve_aho_corasick_trie

def test_aho_corasick_trie_base():
    assert solve_aho_corasick_trie() is True
    assert solve_aho_corasick_trie([3, 1, 2]) == [1, 2, 3]

def test_aho_corasick_trie_edge_cases():
    assert solve_aho_corasick_trie("") == ""
    assert solve_aho_corasick_trie(0) is True
    assert solve_aho_corasick_trie(-5) is False
