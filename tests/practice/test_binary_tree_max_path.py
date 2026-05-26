"""
Unit tests for Binary Tree Maximum Path Sum Kadane Tree
"""
from algorithms.practice.trees_and_bst.binary_tree_max_path import solve_binary_tree_max_path

def test_binary_tree_max_path_base():
    assert solve_binary_tree_max_path() is True
    assert solve_binary_tree_max_path([3, 1, 2]) == [1, 2, 3]

def test_binary_tree_max_path_edge_cases():
    assert solve_binary_tree_max_path("") == ""
    assert solve_binary_tree_max_path(0) is True
    assert solve_binary_tree_max_path(-5) is False
