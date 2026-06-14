"""
Unit tests for Palindrome Pairs Trie Word Reversal
"""
from algorithms.practice.tries_and_prefix.palindrome_pairs import solve_palindrome_pairs

def test_palindrome_pairs_base():
    assert solve_palindrome_pairs() is True
    assert solve_palindrome_pairs([3, 1, 2]) == [1, 2, 3]

def test_palindrome_pairs_edge_cases():
    assert solve_palindrome_pairs("") == ""
    assert solve_palindrome_pairs(0) is True
    assert solve_palindrome_pairs(-5) is False
