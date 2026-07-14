"""
Unit tests for Combination Sum III K Numbers Sum to N
"""
from algorithms.practice.backtracking.combination_sum_iii import solve_combination_sum_iii

def test_combination_sum_iii_base():
    assert solve_combination_sum_iii() is True
    assert solve_combination_sum_iii([3, 1, 2]) == [1, 2, 3]

def test_combination_sum_iii_edge_cases():
    assert solve_combination_sum_iii("") == ""
    assert solve_combination_sum_iii(0) is True
    assert solve_combination_sum_iii(-5) is False
