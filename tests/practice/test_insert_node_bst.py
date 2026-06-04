"""
Unit tests for Insert into a Binary Search Tree
"""
from algorithms.practice.trees_and_bst.insert_node_bst import solve_insert_node_bst

def test_insert_node_bst_base():
    assert solve_insert_node_bst() is True
    assert solve_insert_node_bst([3, 1, 2]) == [1, 2, 3]

def test_insert_node_bst_edge_cases():
    assert solve_insert_node_bst("") == ""
    assert solve_insert_node_bst(0) is True
    assert solve_insert_node_bst(-5) is False
