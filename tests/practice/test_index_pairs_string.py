"""
Unit tests for Index Pairs of a String Trie Traversal
"""
from algorithms.practice.tries_and_prefix.index_pairs_string import solve_index_pairs_string

def test_index_pairs_string_base():
    assert solve_index_pairs_string() is True
    assert solve_index_pairs_string([3, 1, 2]) == [1, 2, 3]

def test_index_pairs_string_edge_cases():
    assert solve_index_pairs_string("") == ""
    assert solve_index_pairs_string(0) is True
    assert solve_index_pairs_string(-5) is False
