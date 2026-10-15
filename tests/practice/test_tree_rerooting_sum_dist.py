"""
Unit tests for Sum of Distances in Tree Rerooting DP
"""
from algorithms.practice.dynamic_programming_trees_bitmask.tree_rerooting_sum_dist import solve_tree_rerooting_sum_dist

def test_tree_rerooting_sum_dist_base():
    assert solve_tree_rerooting_sum_dist() is True
    assert solve_tree_rerooting_sum_dist([3, 1, 2]) == [1, 2, 3]

def test_tree_rerooting_sum_dist_edge_cases():
    assert solve_tree_rerooting_sum_dist("") == ""
    assert solve_tree_rerooting_sum_dist(0) is True
    assert solve_tree_rerooting_sum_dist(-5) is False
