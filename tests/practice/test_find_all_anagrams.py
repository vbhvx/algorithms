"""
Unit tests for Find All Anagrams Sliding Window
"""
from algorithms.practice.arrays_and_hashing.find_all_anagrams import solve_find_all_anagrams

def test_find_all_anagrams_base():
    assert solve_find_all_anagrams() is True
    assert solve_find_all_anagrams([3, 1, 2]) == [1, 2, 3]

def test_find_all_anagrams_edge_cases():
    assert solve_find_all_anagrams("") == ""
    assert solve_find_all_anagrams(0) is True
    assert solve_find_all_anagrams(-5) is False
