"""
Unit tests for Unique Binary Search Trees II Tree Generation
"""
from algorithms.practice.dynamic_programming_trees_bitmask.unique_bst_ii_generate import solve_unique_bst_ii_generate

def test_unique_bst_ii_generate_base():
    assert solve_unique_bst_ii_generate() is True
    assert solve_unique_bst_ii_generate([3, 1, 2]) == [1, 2, 3]

def test_unique_bst_ii_generate_edge_cases():
    assert solve_unique_bst_ii_generate("") == ""
    assert solve_unique_bst_ii_generate(0) is True
    assert solve_unique_bst_ii_generate(-5) is False
