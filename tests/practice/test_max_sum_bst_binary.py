"""
Unit tests for Maximum Sum BST in Binary Tree Subtree Range
"""
from algorithms.practice.dynamic_programming_trees_bitmask.max_sum_bst_binary import solve_max_sum_bst_binary

def test_max_sum_bst_binary_base():
    assert solve_max_sum_bst_binary() is True
    assert solve_max_sum_bst_binary([3, 1, 2]) == [1, 2, 3]

def test_max_sum_bst_binary_edge_cases():
    assert solve_max_sum_bst_binary("") == ""
    assert solve_max_sum_bst_binary(0) is True
    assert solve_max_sum_bst_binary(-5) is False
