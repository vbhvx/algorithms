"""
Unit tests for Lowest Common Ancestor BST Value Property
"""
from algorithms.practice.trees_and_bst.lca_bst import solve_lca_bst

def test_lca_bst_base():
    assert solve_lca_bst() is True
    assert solve_lca_bst([3, 1, 2]) == [1, 2, 3]

def test_lca_bst_edge_cases():
    assert solve_lca_bst("") == ""
    assert solve_lca_bst(0) is True
    assert solve_lca_bst(-5) is False
