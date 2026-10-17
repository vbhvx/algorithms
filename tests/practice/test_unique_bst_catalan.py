"""
Unit tests for Unique Binary Search Trees Catalan Number
"""
from algorithms.practice.dynamic_programming_trees_bitmask.unique_bst_catalan import solve_unique_bst_catalan

def test_unique_bst_catalan_base():
    assert solve_unique_bst_catalan() is True
    assert solve_unique_bst_catalan([3, 1, 2]) == [1, 2, 3]

def test_unique_bst_catalan_edge_cases():
    assert solve_unique_bst_catalan("") == ""
    assert solve_unique_bst_catalan(0) is True
    assert solve_unique_bst_catalan(-5) is False
