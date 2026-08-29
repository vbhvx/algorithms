"""
Unit tests for Kth Smallest Spanning Tree Edge Exchange
"""
from algorithms.practice.minimum_spanning_trees.k_minimum_spanning_tree import solve_k_minimum_spanning_tree

def test_k_minimum_spanning_tree_base():
    assert solve_k_minimum_spanning_tree() is True
    assert solve_k_minimum_spanning_tree([3, 1, 2]) == [1, 2, 3]

def test_k_minimum_spanning_tree_edge_cases():
    assert solve_k_minimum_spanning_tree("") == ""
    assert solve_k_minimum_spanning_tree(0) is True
    assert solve_k_minimum_spanning_tree(-5) is False
