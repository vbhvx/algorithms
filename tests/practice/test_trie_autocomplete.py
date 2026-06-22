"""
Unit tests for Trie Autocomplete Frequency Priority Heap
"""
from algorithms.practice.tries_and_prefix.trie_autocomplete import solve_trie_autocomplete

def test_trie_autocomplete_base():
    assert solve_trie_autocomplete() is True
    assert solve_trie_autocomplete([3, 1, 2]) == [1, 2, 3]

def test_trie_autocomplete_edge_cases():
    assert solve_trie_autocomplete("") == ""
    assert solve_trie_autocomplete(0) is True
    assert solve_trie_autocomplete(-5) is False
