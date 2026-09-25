"""
Unit tests for Longest Common Subsequence 2D Grid
"""
from algorithms.practice.dynamic_programming_2d.longest_common_subseq import solve_longest_common_subseq

def test_longest_common_subseq_base():
    assert solve_longest_common_subseq() is True
    assert solve_longest_common_subseq([3, 1, 2]) == [1, 2, 3]

def test_longest_common_subseq_edge_cases():
    assert solve_longest_common_subseq("") == ""
    assert solve_longest_common_subseq(0) is True
    assert solve_longest_common_subseq(-5) is False
