"""
Unit tests for Sum Root to Leaf Numbers Decimal Shift
"""
from algorithms.practice.trees_and_bst.sum_root_to_leaf import solve_sum_root_to_leaf

def test_sum_root_to_leaf_base():
    assert solve_sum_root_to_leaf() is True
    assert solve_sum_root_to_leaf([3, 1, 2]) == [1, 2, 3]

def test_sum_root_to_leaf_edge_cases():
    assert solve_sum_root_to_leaf("") == ""
    assert solve_sum_root_to_leaf(0) is True
    assert solve_sum_root_to_leaf(-5) is False
