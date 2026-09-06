"""
Unit tests for Dinic Algorithm on Unit Networks Unit Capacities
"""
from algorithms.practice.network_flow_matching.dinic_unit_networks import solve_dinic_unit_networks

def test_dinic_unit_networks_base():
    assert solve_dinic_unit_networks() is True
    assert solve_dinic_unit_networks([3, 1, 2]) == [1, 2, 3]

def test_dinic_unit_networks_edge_cases():
    assert solve_dinic_unit_networks("") == ""
    assert solve_dinic_unit_networks(0) is True
    assert solve_dinic_unit_networks(-5) is False
