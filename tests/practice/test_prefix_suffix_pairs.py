"""
Unit tests for Count Prefix and Suffix Pairs Trie Double Hash
"""
from algorithms.practice.tries_and_prefix.prefix_suffix_pairs import solve_prefix_suffix_pairs

def test_prefix_suffix_pairs_base():
    assert solve_prefix_suffix_pairs() is True
    assert solve_prefix_suffix_pairs([3, 1, 2]) == [1, 2, 3]

def test_prefix_suffix_pairs_edge_cases():
    assert solve_prefix_suffix_pairs("") == ""
    assert solve_prefix_suffix_pairs(0) is True
    assert solve_prefix_suffix_pairs(-5) is False
