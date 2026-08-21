"""
Unit tests for Find Critical and Pseudo-Critical Edges in MST
"""
from algorithms.practice.minimum_spanning_trees.critical_pseudo_edges import solve_critical_pseudo_edges

def test_critical_pseudo_edges_base():
    assert solve_critical_pseudo_edges() is True
    assert solve_critical_pseudo_edges([3, 1, 2]) == [1, 2, 3]

def test_critical_pseudo_edges_edge_cases():
    assert solve_critical_pseudo_edges("") == ""
    assert solve_critical_pseudo_edges(0) is True
    assert solve_critical_pseudo_edges(-5) is False
