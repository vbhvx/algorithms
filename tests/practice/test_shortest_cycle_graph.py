"""
Unit tests for Shortest Cycle in an Undirected Graph BFS
"""
from algorithms.practice.shortest_paths.shortest_cycle_graph import solve_shortest_cycle_graph

def test_shortest_cycle_graph_base():
    assert solve_shortest_cycle_graph() is True
    assert solve_shortest_cycle_graph([3, 1, 2]) == [1, 2, 3]

def test_shortest_cycle_graph_edge_cases():
    assert solve_shortest_cycle_graph("") == ""
    assert solve_shortest_cycle_graph(0) is True
    assert solve_shortest_cycle_graph(-5) is False
