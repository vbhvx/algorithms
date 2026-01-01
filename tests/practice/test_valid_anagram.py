"""
Unit tests for Valid Anagram Counter
"""
from algorithms.practice.arrays_and_hashing.valid_anagram import solve_valid_anagram

def test_valid_anagram_base():
    assert solve_valid_anagram() is True
    assert solve_valid_anagram([3, 1, 2]) == [1, 2, 3]

def test_valid_anagram_edge_cases():
    assert solve_valid_anagram("") == ""
    assert solve_valid_anagram(0) is True
    assert solve_valid_anagram(-5) is False
