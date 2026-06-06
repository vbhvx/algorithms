"""
Unit tests for Flatten Binary Tree to Linked List Preorder
"""
from algorithms.practice.trees_and_bst.flatten_tree_linked import solve_flatten_tree_linked

def test_flatten_tree_linked_base():
    assert solve_flatten_tree_linked() is True
    assert solve_flatten_tree_linked([3, 1, 2]) == [1, 2, 3]

def test_flatten_tree_linked_edge_cases():
    assert solve_flatten_tree_linked("") == ""
    assert solve_flatten_tree_linked(0) is True
    assert solve_flatten_tree_linked(-5) is False
