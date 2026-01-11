"""
Unit tests for Longest Harmonious Subsequence
"""
from algorithms.practice.arrays_and_hashing.longest_harmonic import solve_longest_harmonic

def test_longest_harmonic_base():
    assert solve_longest_harmonic() is True
    assert solve_longest_harmonic([3, 1, 2]) == [1, 2, 3]

def test_longest_harmonic_edge_cases():
    assert solve_longest_harmonic("") == ""
    assert solve_longest_harmonic(0) is True
    assert solve_longest_harmonic(-5) is False
