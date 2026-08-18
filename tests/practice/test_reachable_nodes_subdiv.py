"""
Unit tests for Reachable Nodes in Subdivided Graph Dijkstra
"""
from algorithms.practice.shortest_paths.reachable_nodes_subdiv import solve_reachable_nodes_subdiv

def test_reachable_nodes_subdiv_base():
    assert solve_reachable_nodes_subdiv() is True
    assert solve_reachable_nodes_subdiv([3, 1, 2]) == [1, 2, 3]

def test_reachable_nodes_subdiv_edge_cases():
    assert solve_reachable_nodes_subdiv("") == ""
    assert solve_reachable_nodes_subdiv(0) is True
    assert solve_reachable_nodes_subdiv(-5) is False
