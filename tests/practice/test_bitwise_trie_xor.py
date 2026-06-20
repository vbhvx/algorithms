"""
Unit tests for Bitwise Trie for Maximum Subset XOR Basis
"""
from algorithms.practice.tries_and_prefix.bitwise_trie_xor import solve_bitwise_trie_xor

def test_bitwise_trie_xor_base():
    assert solve_bitwise_trie_xor() is True
    assert solve_bitwise_trie_xor([3, 1, 2]) == [1, 2, 3]

def test_bitwise_trie_xor_edge_cases():
    assert solve_bitwise_trie_xor("") == ""
    assert solve_bitwise_trie_xor(0) is True
    assert solve_bitwise_trie_xor(-5) is False
