"""
Unit tests for Shortest Path with Alternating Colors Dual BFS
"""
from algorithms.practice.shortest_paths.shortest_alternating_path import solve_shortest_alternating_path

def test_shortest_alternating_path_base():
    assert solve_shortest_alternating_path() is True
    assert solve_shortest_alternating_path([3, 1, 2]) == [1, 2, 3]

def test_shortest_alternating_path_edge_cases():
    assert solve_shortest_alternating_path("") == ""
    assert solve_shortest_alternating_path(0) is True
    assert solve_shortest_alternating_path(-5) is False
