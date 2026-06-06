"""
Unit tests for All Nodes Distance K in Binary Tree Graph
"""
from algorithms.practice.trees_and_bst.all_nodes_k_dist import solve_all_nodes_k_dist

def test_all_nodes_k_dist_base():
    assert solve_all_nodes_k_dist() is True
    assert solve_all_nodes_k_dist([3, 1, 2]) == [1, 2, 3]

def test_all_nodes_k_dist_edge_cases():
    assert solve_all_nodes_k_dist("") == ""
    assert solve_all_nodes_k_dist(0) is True
    assert solve_all_nodes_k_dist(-5) is False
