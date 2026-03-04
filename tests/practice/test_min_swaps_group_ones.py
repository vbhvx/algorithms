"""
Unit tests for Minimum Swaps Group All Ones
"""
from algorithms.practice.sliding_window.min_swaps_group_ones import solve_min_swaps_group_ones

def test_min_swaps_group_ones_base():
    assert solve_min_swaps_group_ones() is True
    assert solve_min_swaps_group_ones([3, 1, 2]) == [1, 2, 3]

def test_min_swaps_group_ones_edge_cases():
    assert solve_min_swaps_group_ones("") == ""
    assert solve_min_swaps_group_ones(0) is True
    assert solve_min_swaps_group_ones(-5) is False
