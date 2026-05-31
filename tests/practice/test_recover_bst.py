"""
Unit tests for Recover Binary Search Tree Morris Inorder
"""
from algorithms.practice.trees_and_bst.recover_bst import solve_recover_bst

def test_recover_bst_base():
    assert solve_recover_bst() is True
    assert solve_recover_bst([3, 1, 2]) == [1, 2, 3]

def test_recover_bst_edge_cases():
    assert solve_recover_bst("") == ""
    assert solve_recover_bst(0) is True
    assert solve_recover_bst(-5) is False
