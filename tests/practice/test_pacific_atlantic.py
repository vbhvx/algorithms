"""
Unit tests for Pacific Atlantic Water Flow Inverse Reach
"""
from algorithms.practice.graphs_and_traversals.pacific_atlantic import solve_pacific_atlantic

def test_pacific_atlantic_base():
    assert solve_pacific_atlantic() is True
    assert solve_pacific_atlantic([3, 1, 2]) == [1, 2, 3]

def test_pacific_atlantic_edge_cases():
    assert solve_pacific_atlantic("") == ""
    assert solve_pacific_atlantic(0) is True
    assert solve_pacific_atlantic(-5) is False
