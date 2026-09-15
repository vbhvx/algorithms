"""
Unit tests for Longest Increasing Subsequence Patience Sort
"""
from algorithms.practice.dynamic_programming_1d.lis_patience_sort import solve_lis_patience_sort

def test_lis_patience_sort_base():
    assert solve_lis_patience_sort() is True
    assert solve_lis_patience_sort([3, 1, 2]) == [1, 2, 3]

def test_lis_patience_sort_edge_cases():
    assert solve_lis_patience_sort("") == ""
    assert solve_lis_patience_sort(0) is True
    assert solve_lis_patience_sort(-5) is False
