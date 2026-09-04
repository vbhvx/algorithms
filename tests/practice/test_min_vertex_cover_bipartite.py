"""
Unit tests for Konig Theorem Minimum Vertex Cover Bipartite
"""
from algorithms.practice.network_flow_matching.min_vertex_cover_bipartite import solve_min_vertex_cover_bipartite

def test_min_vertex_cover_bipartite_base():
    assert solve_min_vertex_cover_bipartite() is True
    assert solve_min_vertex_cover_bipartite([3, 1, 2]) == [1, 2, 3]

def test_min_vertex_cover_bipartite_edge_cases():
    assert solve_min_vertex_cover_bipartite("") == ""
    assert solve_min_vertex_cover_bipartite(0) is True
    assert solve_min_vertex_cover_bipartite(-5) is False
