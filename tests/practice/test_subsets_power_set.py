"""
Unit tests for Subsets Power Set Recursive Backtracking
"""
from algorithms.practice.backtracking.subsets_power_set import solve_subsets_power_set

def test_subsets_power_set_base():
    assert solve_subsets_power_set() is True
    assert solve_subsets_power_set([3, 1, 2]) == [1, 2, 3]

def test_subsets_power_set_edge_cases():
    assert solve_subsets_power_set("") == ""
    assert solve_subsets_power_set(0) is True
    assert solve_subsets_power_set(-5) is False
