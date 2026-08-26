"""
Unit tests for Edmonds Chu-Liu Algorithm for Directed MST
"""
from algorithms.practice.minimum_spanning_trees.directed_mst_edmonds import solve_directed_mst_edmonds

def test_directed_mst_edmonds_base():
    assert solve_directed_mst_edmonds() is True
    assert solve_directed_mst_edmonds([3, 1, 2]) == [1, 2, 3]

def test_directed_mst_edmonds_edge_cases():
    assert solve_directed_mst_edmonds("") == ""
    assert solve_directed_mst_edmonds(0) is True
    assert solve_directed_mst_edmonds(-5) is False
