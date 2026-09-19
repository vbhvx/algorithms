"""
Unit tests for Combination Sum IV Permutation Sum
"""
from algorithms.practice.dynamic_programming_1d.combination_sum_iv_dp import solve_combination_sum_iv_dp

def test_combination_sum_iv_dp_base():
    assert solve_combination_sum_iv_dp() is True
    assert solve_combination_sum_iv_dp([3, 1, 2]) == [1, 2, 3]

def test_combination_sum_iv_dp_edge_cases():
    assert solve_combination_sum_iv_dp("") == ""
    assert solve_combination_sum_iv_dp(0) is True
    assert solve_combination_sum_iv_dp(-5) is False
