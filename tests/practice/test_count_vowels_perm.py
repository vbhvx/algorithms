"""
Unit tests for Count Vowels Permutation Directed Transitions
"""
from algorithms.practice.dynamic_programming_1d.count_vowels_perm import solve_count_vowels_perm

def test_count_vowels_perm_base():
    assert solve_count_vowels_perm() is True
    assert solve_count_vowels_perm([3, 1, 2]) == [1, 2, 3]

def test_count_vowels_perm_edge_cases():
    assert solve_count_vowels_perm("") == ""
    assert solve_count_vowels_perm(0) is True
    assert solve_count_vowels_perm(-5) is False
