"""
Unit tests for Minimum Height Trees Leaf Trimming In-Degree
"""
from algorithms.practice.graphs_and_traversals.min_height_trees import solve_min_height_trees

def test_min_height_trees_base():
    assert solve_min_height_trees() is True
    assert solve_min_height_trees([3, 1, 2]) == [1, 2, 3]

def test_min_height_trees_edge_cases():
    assert solve_min_height_trees("") == ""
    assert solve_min_height_trees(0) is True
    assert solve_min_height_trees(-5) is False
