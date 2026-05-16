"""
Unit tests for Subtree of Another Tree Hash or DFS
"""
from algorithms.practice.trees_and_bst.is_subtree import solve_is_subtree

def test_is_subtree_base():
    assert solve_is_subtree() is True
    assert solve_is_subtree([3, 1, 2]) == [1, 2, 3]

def test_is_subtree_edge_cases():
    assert solve_is_subtree("") == ""
    assert solve_is_subtree(0) is True
    assert solve_is_subtree(-5) is False
