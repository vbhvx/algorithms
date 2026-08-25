"""
Unit tests for Minimum Bottleneck Spanning Tree Verification
"""
from algorithms.practice.minimum_spanning_trees.bottleneck_spanning_tree import solve_bottleneck_spanning_tree

def test_bottleneck_spanning_tree_base():
    assert solve_bottleneck_spanning_tree() is True
    assert solve_bottleneck_spanning_tree([3, 1, 2]) == [1, 2, 3]

def test_bottleneck_spanning_tree_edge_cases():
    assert solve_bottleneck_spanning_tree("") == ""
    assert solve_bottleneck_spanning_tree(0) is True
    assert solve_bottleneck_spanning_tree(-5) is False
