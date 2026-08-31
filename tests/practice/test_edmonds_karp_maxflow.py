"""
Unit tests for Edmonds-Karp Max Flow BFS Residual Graph
"""
from algorithms.practice.network_flow_matching.edmonds_karp_maxflow import solve_edmonds_karp_maxflow

def test_edmonds_karp_maxflow_base():
    assert solve_edmonds_karp_maxflow() is True
    assert solve_edmonds_karp_maxflow([3, 1, 2]) == [1, 2, 3]

def test_edmonds_karp_maxflow_edge_cases():
    assert solve_edmonds_karp_maxflow("") == ""
    assert solve_edmonds_karp_maxflow(0) is True
    assert solve_edmonds_karp_maxflow(-5) is False
