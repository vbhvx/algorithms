"""
Unit tests for Maximum Independent Set in Bipartite Graph
"""
from algorithms.practice.network_flow_matching.max_independent_set_bip import solve_max_independent_set_bip

def test_max_independent_set_bip_base():
    assert solve_max_independent_set_bip() is True
    assert solve_max_independent_set_bip([3, 1, 2]) == [1, 2, 3]

def test_max_independent_set_bip_edge_cases():
    assert solve_max_independent_set_bip("") == ""
    assert solve_max_independent_set_bip(0) is True
    assert solve_max_independent_set_bip(-5) is False
