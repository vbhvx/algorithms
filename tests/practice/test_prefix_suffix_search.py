"""
Unit tests for Prefix and Suffix Search Word Filter Trie
"""
from algorithms.practice.tries_and_prefix.prefix_suffix_search import solve_prefix_suffix_search

def test_prefix_suffix_search_base():
    assert solve_prefix_suffix_search() is True
    assert solve_prefix_suffix_search([3, 1, 2]) == [1, 2, 3]

def test_prefix_suffix_search_edge_cases():
    assert solve_prefix_suffix_search("") == ""
    assert solve_prefix_suffix_search(0) is True
    assert solve_prefix_suffix_search(-5) is False
