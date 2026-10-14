"""
Unit tests for Count Special Integers Digit DP Distinct
"""
from algorithms.practice.dynamic_programming_trees_bitmask.count_special_integers import solve_count_special_integers

def test_count_special_integers_base():
    assert solve_count_special_integers() is True
    assert solve_count_special_integers([3, 1, 2]) == [1, 2, 3]

def test_count_special_integers_edge_cases():
    assert solve_count_special_integers("") == ""
    assert solve_count_special_integers(0) is True
    assert solve_count_special_integers(-5) is False
