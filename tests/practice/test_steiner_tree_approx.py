"""
Unit tests for Steiner Tree Minimum Weight Terminal Subgraph
"""
from algorithms.practice.minimum_spanning_trees.steiner_tree_approx import solve_steiner_tree_approx

def test_steiner_tree_approx_base():
    assert solve_steiner_tree_approx() is True
    assert solve_steiner_tree_approx([3, 1, 2]) == [1, 2, 3]

def test_steiner_tree_approx_edge_cases():
    assert solve_steiner_tree_approx("") == ""
    assert solve_steiner_tree_approx(0) is True
    assert solve_steiner_tree_approx(-5) is False
