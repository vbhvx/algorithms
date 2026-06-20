"""
Unit tests for Longest Common Prefix Trie Branch Search
"""
from algorithms.practice.tries_and_prefix.longest_common_prefix import solve_longest_common_prefix

def test_longest_common_prefix_base():
    assert solve_longest_common_prefix() is True
    assert solve_longest_common_prefix([3, 1, 2]) == [1, 2, 3]

def test_longest_common_prefix_edge_cases():
    assert solve_longest_common_prefix("") == ""
    assert solve_longest_common_prefix(0) is True
    assert solve_longest_common_prefix(-5) is False
