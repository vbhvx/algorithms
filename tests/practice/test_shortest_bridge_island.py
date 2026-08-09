"""
Unit tests for Shortest Bridge Two Islands BFS Expansion
"""
from algorithms.practice.graphs_and_traversals.shortest_bridge_island import solve_shortest_bridge_island

def test_shortest_bridge_island_base():
    assert solve_shortest_bridge_island() is True
    assert solve_shortest_bridge_island([3, 1, 2]) == [1, 2, 3]

def test_shortest_bridge_island_edge_cases():
    assert solve_shortest_bridge_island("") == ""
    assert solve_shortest_bridge_island(0) is True
    assert solve_shortest_bridge_island(-5) is False
