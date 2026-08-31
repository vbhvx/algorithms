"""
Unit tests for Ford-Fulkerson Max Flow Augmenting Paths
"""
from algorithms.practice.network_flow_matching.ford_fulkerson_dfs import solve_ford_fulkerson_dfs

def test_ford_fulkerson_dfs_base():
    assert solve_ford_fulkerson_dfs() is True
    assert solve_ford_fulkerson_dfs([3, 1, 2]) == [1, 2, 3]

def test_ford_fulkerson_dfs_edge_cases():
    assert solve_ford_fulkerson_dfs("") == ""
    assert solve_ford_fulkerson_dfs(0) is True
    assert solve_ford_fulkerson_dfs(-5) is False
