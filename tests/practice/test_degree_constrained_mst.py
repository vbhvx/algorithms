"""
Unit tests for Degree-Constrained MST Heuristic Approximation
"""
from algorithms.practice.minimum_spanning_trees.degree_constrained_mst import solve_degree_constrained_mst

def test_degree_constrained_mst_base():
    assert solve_degree_constrained_mst() is True
    assert solve_degree_constrained_mst([3, 1, 2]) == [1, 2, 3]

def test_degree_constrained_mst_edge_cases():
    assert solve_degree_constrained_mst("") == ""
    assert solve_degree_constrained_mst(0) is True
    assert solve_degree_constrained_mst(-5) is False
