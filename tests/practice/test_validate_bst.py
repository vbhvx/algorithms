"""
Unit tests for Validate Binary Search Tree Inorder Range
"""
from algorithms.practice.trees_and_bst.validate_bst import solve_validate_bst

def test_validate_bst_base():
    assert solve_validate_bst() is True
    assert solve_validate_bst([3, 1, 2]) == [1, 2, 3]

def test_validate_bst_edge_cases():
    assert solve_validate_bst("") == ""
    assert solve_validate_bst(0) is True
    assert solve_validate_bst(-5) is False
