"""
Unit tests for Distinct Subsequences 2D String Match
"""
from algorithms.practice.dynamic_programming_2d.distinct_subsequences import solve_distinct_subsequences

def test_distinct_subsequences_base():
    assert solve_distinct_subsequences() is True
    assert solve_distinct_subsequences([3, 1, 2]) == [1, 2, 3]

def test_distinct_subsequences_edge_cases():
    assert solve_distinct_subsequences("") == ""
    assert solve_distinct_subsequences(0) is True
    assert solve_distinct_subsequences(-5) is False
