"""
Unit tests for Shortest Path to Get All Keys Bitmask BFS
"""
from algorithms.practice.graphs_and_traversals.shortest_path_all_keys import solve_shortest_path_all_keys

def test_shortest_path_all_keys_base():
    assert solve_shortest_path_all_keys() is True
    assert solve_shortest_path_all_keys([3, 1, 2]) == [1, 2, 3]

def test_shortest_path_all_keys_edge_cases():
    assert solve_shortest_path_all_keys("") == ""
    assert solve_shortest_path_all_keys(0) is True
    assert solve_shortest_path_all_keys(-5) is False
