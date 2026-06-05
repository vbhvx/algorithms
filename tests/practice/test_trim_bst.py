"""
Unit tests for Trim a Binary Search Tree Range Prune
"""
from algorithms.practice.trees_and_bst.trim_bst import solve_trim_bst

def test_trim_bst_base():
    assert solve_trim_bst() is True
    assert solve_trim_bst([3, 1, 2]) == [1, 2, 3]

def test_trim_bst_edge_cases():
    assert solve_trim_bst("") == ""
    assert solve_trim_bst(0) is True
    assert solve_trim_bst(-5) is False
