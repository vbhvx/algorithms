"""
Unit tests for Bellman Ford Shortest Path Negative Cycles
"""
from algorithms.practice.shortest_paths.bellman_ford_neg import solve_bellman_ford_neg

def test_bellman_ford_neg_base():
    assert solve_bellman_ford_neg() is True
    assert solve_bellman_ford_neg([3, 1, 2]) == [1, 2, 3]

def test_bellman_ford_neg_edge_cases():
    assert solve_bellman_ford_neg("") == ""
    assert solve_bellman_ford_neg(0) is True
    assert solve_bellman_ford_neg(-5) is False
