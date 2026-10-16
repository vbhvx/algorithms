"""
Unit tests for All Possible Full Binary Trees Catalan DP
"""
from algorithms.practice.dynamic_programming_trees_bitmask.all_possible_full_binary import solve_all_possible_full_binary

def test_all_possible_full_binary_base():
    assert solve_all_possible_full_binary() is True
    assert solve_all_possible_full_binary([3, 1, 2]) == [1, 2, 3]

def test_all_possible_full_binary_edge_cases():
    assert solve_all_possible_full_binary("") == ""
    assert solve_all_possible_full_binary(0) is True
    assert solve_all_possible_full_binary(-5) is False
