"""
Unit tests for 3Sum Zero Triplet Two Pointers
"""
from algorithms.practice.two_pointers.three_sum import solve_three_sum

def test_three_sum_base():
    assert solve_three_sum() is True
    assert solve_three_sum([3, 1, 2]) == [1, 2, 3]

def test_three_sum_edge_cases():
    assert solve_three_sum("") == ""
    assert solve_three_sum(0) is True
    assert solve_three_sum(-5) is False
