"""
Unit tests for Construct Binary Tree from Inorder Postorder
"""
from algorithms.practice.trees_and_bst.construct_in_post import solve_construct_in_post

def test_construct_in_post_base():
    assert solve_construct_in_post() is True
    assert solve_construct_in_post([3, 1, 2]) == [1, 2, 3]

def test_construct_in_post_edge_cases():
    assert solve_construct_in_post("") == ""
    assert solve_construct_in_post(0) is True
    assert solve_construct_in_post(-5) is False
