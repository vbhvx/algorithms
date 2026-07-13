"""
Unit tests for Combination Sum Unlimited Candidates
"""
from algorithms.practice.backtracking.combination_sum import solve_combination_sum

def test_combination_sum_base():
    assert solve_combination_sum() is True
    assert solve_combination_sum([3, 1, 2]) == [1, 2, 3]

def test_combination_sum_edge_cases():
    assert solve_combination_sum("") == ""
    assert solve_combination_sum(0) is True
    assert solve_combination_sum(-5) is False
