"""
Unit tests for Dinic Max Flow Level Graph Blocking Flow
"""
from algorithms.practice.network_flow_matching.dinic_algorithm_flow import solve_dinic_algorithm_flow

def test_dinic_algorithm_flow_base():
    assert solve_dinic_algorithm_flow() is True
    assert solve_dinic_algorithm_flow([3, 1, 2]) == [1, 2, 3]

def test_dinic_algorithm_flow_edge_cases():
    assert solve_dinic_algorithm_flow("") == ""
    assert solve_dinic_algorithm_flow(0) is True
    assert solve_dinic_algorithm_flow(-5) is False
