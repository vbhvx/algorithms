"""
Unit tests for Aggressive Cows Maximum Minimum Distance
"""
from algorithms.practice.binary_search.aggressive_cows import solve_aggressive_cows

def test_aggressive_cows_base():
    assert solve_aggressive_cows() is True
    assert solve_aggressive_cows([3, 1, 2]) == [1, 2, 3]

def test_aggressive_cows_edge_cases():
    assert solve_aggressive_cows("") == ""
    assert solve_aggressive_cows(0) is True
    assert solve_aggressive_cows(-5) is False
