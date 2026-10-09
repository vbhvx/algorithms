"""
Unit tests for Diameter of General Tree Rerooting DP
"""
from algorithms.practice.dynamic_programming_trees_bitmask.tree_diameter_general import solve_tree_diameter_general

def test_tree_diameter_general_base():
    assert solve_tree_diameter_general() is True
    assert solve_tree_diameter_general([3, 1, 2]) == [1, 2, 3]

def test_tree_diameter_general_edge_cases():
    assert solve_tree_diameter_general("") == ""
    assert solve_tree_diameter_general(0) is True
    assert solve_tree_diameter_general(-5) is False
