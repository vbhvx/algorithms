"""
Unit tests for Same Tree Structural Equivalence
"""
from algorithms.practice.trees_and_bst.is_same_tree import solve_is_same_tree

def test_is_same_tree_base():
    assert solve_is_same_tree() is True
    assert solve_is_same_tree([3, 1, 2]) == [1, 2, 3]

def test_is_same_tree_edge_cases():
    assert solve_is_same_tree("") == ""
    assert solve_is_same_tree(0) is True
    assert solve_is_same_tree(-5) is False
