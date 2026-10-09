"""
Unit tests for House Robber III Include Exclude Subtree
"""
from algorithms.practice.dynamic_programming_trees_bitmask.house_robber_iii_tree import solve_house_robber_iii_tree

def test_house_robber_iii_tree_base():
    assert solve_house_robber_iii_tree() is True
    assert solve_house_robber_iii_tree([3, 1, 2]) == [1, 2, 3]

def test_house_robber_iii_tree_edge_cases():
    assert solve_house_robber_iii_tree("") == ""
    assert solve_house_robber_iii_tree(0) is True
    assert solve_house_robber_iii_tree(-5) is False
