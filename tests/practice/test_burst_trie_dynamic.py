"""
Unit tests for Burst Trie Dynamic Container Optimization
"""
from algorithms.practice.tries_and_prefix.burst_trie_dynamic import solve_burst_trie_dynamic

def test_burst_trie_dynamic_base():
    assert solve_burst_trie_dynamic() is True
    assert solve_burst_trie_dynamic([3, 1, 2]) == [1, 2, 3]

def test_burst_trie_dynamic_edge_cases():
    assert solve_burst_trie_dynamic("") == ""
    assert solve_burst_trie_dynamic(0) is True
    assert solve_burst_trie_dynamic(-5) is False
