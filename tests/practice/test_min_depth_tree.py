"""
Unit tests for Minimum Depth of Binary Tree BFS
"""
from algorithms.practice.trees_and_bst.min_depth_tree import solve_min_depth_tree

def test_min_depth_tree_base():
    assert solve_min_depth_tree() is True
    assert solve_min_depth_tree([3, 1, 2]) == [1, 2, 3]

def test_min_depth_tree_edge_cases():
    assert solve_min_depth_tree("") == ""
    assert solve_min_depth_tree(0) is True
    assert solve_min_depth_tree(-5) is False
