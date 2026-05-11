"""
Unit tests for Invert Binary Tree Recursive DFS
"""
from algorithms.practice.trees_and_bst.invert_binary_tree import solve_invert_binary_tree

def test_invert_binary_tree_base():
    assert solve_invert_binary_tree() is True
    assert solve_invert_binary_tree([3, 1, 2]) == [1, 2, 3]

def test_invert_binary_tree_edge_cases():
    assert solve_invert_binary_tree("") == ""
    assert solve_invert_binary_tree(0) is True
    assert solve_invert_binary_tree(-5) is False
