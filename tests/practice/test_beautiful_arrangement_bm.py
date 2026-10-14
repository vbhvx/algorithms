"""
Unit tests for Beautiful Arrangement Bitmask DP
"""
from algorithms.practice.dynamic_programming_trees_bitmask.beautiful_arrangement_bm import solve_beautiful_arrangement_bm

def test_beautiful_arrangement_bm_base():
    assert solve_beautiful_arrangement_bm() is True
    assert solve_beautiful_arrangement_bm([3, 1, 2]) == [1, 2, 3]

def test_beautiful_arrangement_bm_edge_cases():
    assert solve_beautiful_arrangement_bm("") == ""
    assert solve_beautiful_arrangement_bm(0) is True
    assert solve_beautiful_arrangement_bm(-5) is False
