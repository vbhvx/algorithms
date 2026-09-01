"""
Unit tests for Kuhn Hungarian Algorithm Maximum Bipartite
"""
from algorithms.practice.network_flow_matching.kuhn_bipartite_match import solve_kuhn_bipartite_match

def test_kuhn_bipartite_match_base():
    assert solve_kuhn_bipartite_match() is True
    assert solve_kuhn_bipartite_match([3, 1, 2]) == [1, 2, 3]

def test_kuhn_bipartite_match_edge_cases():
    assert solve_kuhn_bipartite_match("") == ""
    assert solve_kuhn_bipartite_match(0) is True
    assert solve_kuhn_bipartite_match(-5) is False
