"""
Unit tests for Network Delay Time Dijkstra Broadcast
"""
from algorithms.practice.shortest_paths.network_delay_time import solve_network_delay_time

def test_network_delay_time_base():
    assert solve_network_delay_time() is True
    assert solve_network_delay_time([3, 1, 2]) == [1, 2, 3]

def test_network_delay_time_edge_cases():
    assert solve_network_delay_time("") == ""
    assert solve_network_delay_time(0) is True
    assert solve_network_delay_time(-5) is False
