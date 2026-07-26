"""
Unit tests for Clone Graph Undirected Hash Map Traversal
"""
from algorithms.practice.graphs_and_traversals.clone_graph_hash import solve_clone_graph_hash

def test_clone_graph_hash_base():
    assert solve_clone_graph_hash() is True
    assert solve_clone_graph_hash([3, 1, 2]) == [1, 2, 3]

def test_clone_graph_hash_edge_cases():
    assert solve_clone_graph_hash("") == ""
    assert solve_clone_graph_hash(0) is True
    assert solve_clone_graph_hash(-5) is False
