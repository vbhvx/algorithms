"""
Unit tests for Case Insensitive Trie Canonical Index
"""
from algorithms.practice.tries_and_prefix.trie_case_insensitive import solve_trie_case_insensitive

def test_trie_case_insensitive_base():
    assert solve_trie_case_insensitive() is True
    assert solve_trie_case_insensitive([3, 1, 2]) == [1, 2, 3]

def test_trie_case_insensitive_edge_cases():
    assert solve_trie_case_insensitive("") == ""
    assert solve_trie_case_insensitive(0) is True
    assert solve_trie_case_insensitive(-5) is False
