"""
Unit tests for Maximum Product of Splitted Binary Tree
"""
from algorithms.practice.dynamic_programming_trees_bitmask.maximum_product_tree_split import solve_maximum_product_tree_split

def test_maximum_product_tree_split_base():
    assert solve_maximum_product_tree_split() is True
    assert solve_maximum_product_tree_split([3, 1, 2]) == [1, 2, 3]

def test_maximum_product_tree_split_edge_cases():
    assert solve_maximum_product_tree_split("") == ""
    assert solve_maximum_product_tree_split(0) is True
    assert solve_maximum_product_tree_split(-5) is False
