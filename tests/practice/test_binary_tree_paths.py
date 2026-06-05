"""
Unit tests for Binary Tree Paths String Construction
"""
from algorithms.practice.trees_and_bst.binary_tree_paths import solve_binary_tree_paths

def test_binary_tree_paths_base():
    assert solve_binary_tree_paths() is True
    assert solve_binary_tree_paths([3, 1, 2]) == [1, 2, 3]

def test_binary_tree_paths_edge_cases():
    assert solve_binary_tree_paths("") == ""
    assert solve_binary_tree_paths(0) is True
    assert solve_binary_tree_paths(-5) is False
