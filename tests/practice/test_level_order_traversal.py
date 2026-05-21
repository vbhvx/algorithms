"""
Unit tests for Binary Tree Level Order Traversal BFS
"""
from algorithms.practice.trees_and_bst.level_order_traversal import solve_level_order_traversal

def test_level_order_traversal_base():
    assert solve_level_order_traversal() is True
    assert solve_level_order_traversal([3, 1, 2]) == [1, 2, 3]

def test_level_order_traversal_edge_cases():
    assert solve_level_order_traversal("") == ""
    assert solve_level_order_traversal(0) is True
    assert solve_level_order_traversal(-5) is False
