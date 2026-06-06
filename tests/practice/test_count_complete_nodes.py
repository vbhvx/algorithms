"""
Unit tests for Count Complete Tree Nodes Log Squared
"""
from algorithms.practice.trees_and_bst.count_complete_nodes import solve_count_complete_nodes

def test_count_complete_nodes_base():
    assert solve_count_complete_nodes() is True
    assert solve_count_complete_nodes([3, 1, 2]) == [1, 2, 3]

def test_count_complete_nodes_edge_cases():
    assert solve_count_complete_nodes("") == ""
    assert solve_count_complete_nodes(0) is True
    assert solve_count_complete_nodes(-5) is False
