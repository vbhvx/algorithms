"""
Unit tests for Compact Prefix Tree Memory Optimization
"""
from algorithms.practice.tries_and_prefix.compact_prefix_tree import solve_compact_prefix_tree

def test_compact_prefix_tree_base():
    assert solve_compact_prefix_tree() is True
    assert solve_compact_prefix_tree([3, 1, 2]) == [1, 2, 3]

def test_compact_prefix_tree_edge_cases():
    assert solve_compact_prefix_tree("") == ""
    assert solve_compact_prefix_tree(0) is True
    assert solve_compact_prefix_tree(-5) is False
