"""
Unit tests for Binary Search Tree Iterator Controlled Stack
"""
from algorithms.practice.trees_and_bst.bst_iterator import solve_bst_iterator

def test_bst_iterator_base():
    assert solve_bst_iterator() is True
    assert solve_bst_iterator([3, 1, 2]) == [1, 2, 3]

def test_bst_iterator_edge_cases():
    assert solve_bst_iterator("") == ""
    assert solve_bst_iterator(0) is True
    assert solve_bst_iterator(-5) is False
