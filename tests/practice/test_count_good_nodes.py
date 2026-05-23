"""
Unit tests for Count Good Nodes in Binary Tree Max Path
"""
from algorithms.practice.trees_and_bst.count_good_nodes import solve_count_good_nodes

def test_count_good_nodes_base():
    assert solve_count_good_nodes() is True
    assert solve_count_good_nodes([3, 1, 2]) == [1, 2, 3]

def test_count_good_nodes_edge_cases():
    assert solve_count_good_nodes("") == ""
    assert solve_count_good_nodes(0) is True
    assert solve_count_good_nodes(-5) is False
