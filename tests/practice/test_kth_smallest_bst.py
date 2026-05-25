"""
Unit tests for Kth Smallest Element in BST Inorder
"""
from algorithms.practice.trees_and_bst.kth_smallest_bst import solve_kth_smallest_bst

def test_kth_smallest_bst_base():
    assert solve_kth_smallest_bst() is True
    assert solve_kth_smallest_bst([3, 1, 2]) == [1, 2, 3]

def test_kth_smallest_bst_edge_cases():
    assert solve_kth_smallest_bst("") == ""
    assert solve_kth_smallest_bst(0) is True
    assert solve_kth_smallest_bst(-5) is False
