"""
Unit tests for Min Cost Max Flow SPFA Augmenting Paths
"""
from algorithms.practice.network_flow_matching.min_cost_max_flow_spfa import solve_min_cost_max_flow_spfa

def test_min_cost_max_flow_spfa_base():
    assert solve_min_cost_max_flow_spfa() is True
    assert solve_min_cost_max_flow_spfa([3, 1, 2]) == [1, 2, 3]

def test_min_cost_max_flow_spfa_edge_cases():
    assert solve_min_cost_max_flow_spfa("") == ""
    assert solve_min_cost_max_flow_spfa(0) is True
    assert solve_min_cost_max_flow_spfa(-5) is False
