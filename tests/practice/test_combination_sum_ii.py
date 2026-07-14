"""
Unit tests for Combination Sum II Single Use Duplicates
"""
from algorithms.practice.backtracking.combination_sum_ii import solve_combination_sum_ii

def test_combination_sum_ii_base():
    assert solve_combination_sum_ii() is True
    assert solve_combination_sum_ii([3, 1, 2]) == [1, 2, 3]

def test_combination_sum_ii_edge_cases():
    assert solve_combination_sum_ii("") == ""
    assert solve_combination_sum_ii(0) is True
    assert solve_combination_sum_ii(-5) is False
