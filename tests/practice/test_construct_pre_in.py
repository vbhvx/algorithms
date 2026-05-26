"""
Unit tests for Construct Binary Tree from Preorder Inorder
"""
from algorithms.practice.trees_and_bst.construct_pre_in import solve_construct_pre_in

def test_construct_pre_in_base():
    assert solve_construct_pre_in() is True
    assert solve_construct_pre_in([3, 1, 2]) == [1, 2, 3]

def test_construct_pre_in_edge_cases():
    assert solve_construct_pre_in("") == ""
    assert solve_construct_pre_in(0) is True
    assert solve_construct_pre_in(-5) is False
