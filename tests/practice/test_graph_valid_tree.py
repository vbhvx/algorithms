"""
Unit tests for Graph Valid Tree Cycle & Connectivity
"""
from algorithms.practice.graphs_and_traversals.graph_valid_tree import solve_graph_valid_tree

def test_graph_valid_tree_base():
    assert solve_graph_valid_tree() is True
    assert solve_graph_valid_tree([3, 1, 2]) == [1, 2, 3]

def test_graph_valid_tree_edge_cases():
    assert solve_graph_valid_tree("") == ""
    assert solve_graph_valid_tree(0) is True
    assert solve_graph_valid_tree(-5) is False
