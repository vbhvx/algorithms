"""
Unit tests for Design Graph With Shortest Path Calculator
"""
from algorithms.practice.shortest_paths.design_graph_dijkstra import solve_design_graph_dijkstra

def test_design_graph_dijkstra_base():
    assert solve_design_graph_dijkstra() is True
    assert solve_design_graph_dijkstra([3, 1, 2]) == [1, 2, 3]

def test_design_graph_dijkstra_edge_cases():
    assert solve_design_graph_dijkstra("") == ""
    assert solve_design_graph_dijkstra(0) is True
    assert solve_design_graph_dijkstra(-5) is False
