"""
Unit tests for Suffix Trie for Longest Common Substring
"""
from algorithms.practice.tries_and_prefix.suffix_trie_lcp import solve_suffix_trie_lcp

def test_suffix_trie_lcp_base():
    assert solve_suffix_trie_lcp() is True
    assert solve_suffix_trie_lcp([3, 1, 2]) == [1, 2, 3]

def test_suffix_trie_lcp_edge_cases():
    assert solve_suffix_trie_lcp("") == ""
    assert solve_suffix_trie_lcp(0) is True
    assert solve_suffix_trie_lcp(-5) is False
