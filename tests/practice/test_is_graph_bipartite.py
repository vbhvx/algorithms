"""
Unit tests for Is Graph Bipartite 2-Coloring BFS
"""
from algorithms.practice.graphs_and_traversals.is_graph_bipartite import solve_is_graph_bipartite

def test_is_graph_bipartite_base():
    assert solve_is_graph_bipartite() is True
    assert solve_is_graph_bipartite([3, 1, 2]) == [1, 2, 3]

def test_is_graph_bipartite_edge_cases():
    assert solve_is_graph_bipartite("") == ""
    assert solve_is_graph_bipartite(0) is True
    assert solve_is_graph_bipartite(-5) is False
