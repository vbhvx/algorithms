"""
Unit tests for Delete Node in BST Inorder Successor
"""
from algorithms.practice.trees_and_bst.delete_node_bst import solve_delete_node_bst

def test_delete_node_bst_base():
    assert solve_delete_node_bst() is True
    assert solve_delete_node_bst([3, 1, 2]) == [1, 2, 3]

def test_delete_node_bst_edge_cases():
    assert solve_delete_node_bst("") == ""
    assert solve_delete_node_bst(0) is True
    assert solve_delete_node_bst(-5) is False
