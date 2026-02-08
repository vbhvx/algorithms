"""
Unit tests for Reverse Vowels of String
"""
from algorithms.practice.two_pointers.reverse_vowels import solve_reverse_vowels

def test_reverse_vowels_base():
    assert solve_reverse_vowels() is True
    assert solve_reverse_vowels([3, 1, 2]) == [1, 2, 3]

def test_reverse_vowels_edge_cases():
    assert solve_reverse_vowels("") == ""
    assert solve_reverse_vowels(0) is True
    assert solve_reverse_vowels(-5) is False
