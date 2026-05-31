"""
Unit tests for Binary Tree Zigzag Level Order Traversal
"""
from algorithms.practice.trees_and_bst.zigzag_level_order import solve_zigzag_level_order

def test_zigzag_level_order_base():
    assert solve_zigzag_level_order() is True
    assert solve_zigzag_level_order([3, 1, 2]) == [1, 2, 3]

def test_zigzag_level_order_edge_cases():
    assert solve_zigzag_level_order("") == ""
    assert solve_zigzag_level_order(0) is True
    assert solve_zigzag_level_order(-5) is False
