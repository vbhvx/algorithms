"""
Unit tests for Binary Tree Right Side View Level Order
"""
from algorithms.practice.trees_and_bst.right_side_view import solve_right_side_view

def test_right_side_view_base():
    assert solve_right_side_view() is True
    assert solve_right_side_view([3, 1, 2]) == [1, 2, 3]

def test_right_side_view_edge_cases():
    assert solve_right_side_view("") == ""
    assert solve_right_side_view(0) is True
    assert solve_right_side_view(-5) is False
