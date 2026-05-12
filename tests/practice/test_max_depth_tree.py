"""
Unit tests for Maximum Depth of Binary Tree
"""
from algorithms.practice.trees_and_bst.max_depth_tree import solve_max_depth_tree

def test_max_depth_tree_base():
    assert solve_max_depth_tree() is True
    assert solve_max_depth_tree([3, 1, 2]) == [1, 2, 3]

def test_max_depth_tree_edge_cases():
    assert solve_max_depth_tree("") == ""
    assert solve_max_depth_tree(0) is True
    assert solve_max_depth_tree(-5) is False
