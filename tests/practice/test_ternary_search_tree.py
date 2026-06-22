"""
Unit tests for Ternary Search Tree Three-Way Branching
"""
from algorithms.practice.tries_and_prefix.ternary_search_tree import solve_ternary_search_tree

def test_ternary_search_tree_base():
    assert solve_ternary_search_tree() is True
    assert solve_ternary_search_tree([3, 1, 2]) == [1, 2, 3]

def test_ternary_search_tree_edge_cases():
    assert solve_ternary_search_tree("") == ""
    assert solve_ternary_search_tree(0) is True
    assert solve_ternary_search_tree(-5) is False
