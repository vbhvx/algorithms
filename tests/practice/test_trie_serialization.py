"""
Unit tests for Trie Serialization to Compact Byte Array
"""
from algorithms.practice.tries_and_prefix.trie_serialization import solve_trie_serialization

def test_trie_serialization_base():
    assert solve_trie_serialization() is True
    assert solve_trie_serialization([3, 1, 2]) == [1, 2, 3]

def test_trie_serialization_edge_cases():
    assert solve_trie_serialization("") == ""
    assert solve_trie_serialization(0) is True
    assert solve_trie_serialization(-5) is False
