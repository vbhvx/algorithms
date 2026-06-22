"""
Unit tests for Radix Tree Compressed Edge Trie
"""
from algorithms.practice.tries_and_prefix.radix_tree_compressed import solve_radix_tree_compressed

def test_radix_tree_compressed_base():
    assert solve_radix_tree_compressed() is True
    assert solve_radix_tree_compressed([3, 1, 2]) == [1, 2, 3]

def test_radix_tree_compressed_edge_cases():
    assert solve_radix_tree_compressed("") == ""
    assert solve_radix_tree_compressed(0) is True
    assert solve_radix_tree_compressed(-5) is False
