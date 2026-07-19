"""
Unit tests for Non-Decreasing Subsequences Hash Visited
"""
from algorithms.practice.backtracking.non_decreasing_subseq import solve_non_decreasing_subseq

def test_non_decreasing_subseq_base():
    assert solve_non_decreasing_subseq() is True
    assert solve_non_decreasing_subseq([3, 1, 2]) == [1, 2, 3]

def test_non_decreasing_subseq_edge_cases():
    assert solve_non_decreasing_subseq("") == ""
    assert solve_non_decreasing_subseq(0) is True
    assert solve_non_decreasing_subseq(-5) is False
