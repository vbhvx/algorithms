"""
Unit tests for Bipartite Edge Coloring Vizing Degree
"""
from algorithms.practice.network_flow_matching.bipartite_edge_coloring import solve_bipartite_edge_coloring

def test_bipartite_edge_coloring_base():
    assert solve_bipartite_edge_coloring() is True
    assert solve_bipartite_edge_coloring([3, 1, 2]) == [1, 2, 3]

def test_bipartite_edge_coloring_edge_cases():
    assert solve_bipartite_edge_coloring("") == ""
    assert solve_bipartite_edge_coloring(0) is True
    assert solve_bipartite_edge_coloring(-5) is False
