"""
Unit tests for Bus Routes Breadth-First Route Graph
"""
from algorithms.practice.graphs_and_traversals.bus_routes_bfs import solve_bus_routes_bfs

def test_bus_routes_bfs_base():
    assert solve_bus_routes_bfs() is True
    assert solve_bus_routes_bfs([3, 1, 2]) == [1, 2, 3]

def test_bus_routes_bfs_edge_cases():
    assert solve_bus_routes_bfs("") == ""
    assert solve_bus_routes_bfs(0) is True
    assert solve_bus_routes_bfs(-5) is False
