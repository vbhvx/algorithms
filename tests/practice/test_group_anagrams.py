"""
Unit tests for Group Anagrams Sorted Key
"""
from algorithms.practice.arrays_and_hashing.group_anagrams import solve_group_anagrams

def test_group_anagrams_base():
    assert solve_group_anagrams() is True
    assert solve_group_anagrams([3, 1, 2]) == [1, 2, 3]

def test_group_anagrams_edge_cases():
    assert solve_group_anagrams("") == ""
    assert solve_group_anagrams(0) is True
    assert solve_group_anagrams(-5) is False
