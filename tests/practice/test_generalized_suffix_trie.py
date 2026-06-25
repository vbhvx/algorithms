"""
Unit tests for Generalized Suffix Trie Multi-String Match
"""
from algorithms.practice.tries_and_prefix.generalized_suffix_trie import solve_generalized_suffix_trie

def test_generalized_suffix_trie_base():
    assert solve_generalized_suffix_trie() is True
    assert solve_generalized_suffix_trie([3, 1, 2]) == [1, 2, 3]

def test_generalized_suffix_trie_edge_cases():
    assert solve_generalized_suffix_trie("") == ""
    assert solve_generalized_suffix_trie(0) is True
    assert solve_generalized_suffix_trie(-5) is False
