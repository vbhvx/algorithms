"""
Unit tests for 4Sum Quadruplet Two Pointers
"""
from algorithms.practice.two_pointers.four_sum import solve_four_sum

def test_four_sum_base():
    assert solve_four_sum() is True
    assert solve_four_sum([3, 1, 2]) == [1, 2, 3]

def test_four_sum_edge_cases():
    assert solve_four_sum("") == ""
    assert solve_four_sum(0) is True
    assert solve_four_sum(-5) is False
