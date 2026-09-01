"""
Unit tests for Hopcroft-Karp Maximum Bipartite Matching
"""
from algorithms.practice.network_flow_matching.bipartite_hopcroft_karp import solve_bipartite_hopcroft_karp

def test_bipartite_hopcroft_karp_base():
    assert solve_bipartite_hopcroft_karp() is True
    assert solve_bipartite_hopcroft_karp([3, 1, 2]) == [1, 2, 3]

def test_bipartite_hopcroft_karp_edge_cases():
    assert solve_bipartite_hopcroft_karp("") == ""
    assert solve_bipartite_hopcroft_karp(0) is True
    assert solve_bipartite_hopcroft_karp(-5) is False
