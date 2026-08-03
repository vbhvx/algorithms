"""
Unit tests for Redundant Connection Disjoint Set Union
"""
from algorithms.practice.graphs_and_traversals.redundant_connection import solve_redundant_connection

def test_redundant_connection_base():
    assert solve_redundant_connection() is True
    assert solve_redundant_connection([3, 1, 2]) == [1, 2, 3]

def test_redundant_connection_edge_cases():
    assert solve_redundant_connection("") == ""
    assert solve_redundant_connection(0) is True
    assert solve_redundant_connection(-5) is False
