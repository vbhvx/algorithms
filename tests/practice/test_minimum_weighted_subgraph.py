"""
Unit tests for Minimum Weighted Subgraph with Required Paths
"""
from algorithms.practice.shortest_paths.minimum_weighted_subgraph import solve_minimum_weighted_subgraph

def test_minimum_weighted_subgraph_base():
    assert solve_minimum_weighted_subgraph() is True
    assert solve_minimum_weighted_subgraph([3, 1, 2]) == [1, 2, 3]

def test_minimum_weighted_subgraph_edge_cases():
    assert solve_minimum_weighted_subgraph("") == ""
    assert solve_minimum_weighted_subgraph(0) is True
    assert solve_minimum_weighted_subgraph(-5) is False
