"""
Unit tests for Binary Tree Cameras Tree DP Vertex Cover
"""
from algorithms.practice.dynamic_programming_trees_bitmask.tree_cameras_greedy import solve_tree_cameras_greedy

def test_tree_cameras_greedy_base():
    assert solve_tree_cameras_greedy() is True
    assert solve_tree_cameras_greedy([3, 1, 2]) == [1, 2, 3]

def test_tree_cameras_greedy_edge_cases():
    assert solve_tree_cameras_greedy("") == ""
    assert solve_tree_cameras_greedy(0) is True
    assert solve_tree_cameras_greedy(-5) is False
