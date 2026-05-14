"""
Unit tests for Diameter of Binary Tree Postorder
"""
from algorithms.practice.trees_and_bst.diameter_binary_tree import solve_diameter_binary_tree

def test_diameter_binary_tree_base():
    assert solve_diameter_binary_tree() is True
    assert solve_diameter_binary_tree([3, 1, 2]) == [1, 2, 3]

def test_diameter_binary_tree_edge_cases():
    assert solve_diameter_binary_tree("") == ""
    assert solve_diameter_binary_tree(0) is True
    assert solve_diameter_binary_tree(-5) is False
