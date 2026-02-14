"""
Unit tests for Permutation in String Window
"""
from algorithms.practice.sliding_window.permutation_string import solve_permutation_string

def test_permutation_string_base():
    assert solve_permutation_string() is True
    assert solve_permutation_string([3, 1, 2]) == [1, 2, 3]

def test_permutation_string_edge_cases():
    assert solve_permutation_string("") == ""
    assert solve_permutation_string(0) is True
    assert solve_permutation_string(-5) is False
