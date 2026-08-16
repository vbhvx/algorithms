"""
Unit tests for Shortest Path Visiting All Nodes Bitmask BFS
"""
from algorithms.practice.shortest_paths.shortest_path_all_nodes import solve_shortest_path_all_nodes

def test_shortest_path_all_nodes_base():
    assert solve_shortest_path_all_nodes() is True
    assert solve_shortest_path_all_nodes([3, 1, 2]) == [1, 2, 3]

def test_shortest_path_all_nodes_edge_cases():
    assert solve_shortest_path_all_nodes("") == ""
    assert solve_shortest_path_all_nodes(0) is True
    assert solve_shortest_path_all_nodes(-5) is False
