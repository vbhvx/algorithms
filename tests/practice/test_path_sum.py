"""
Unit tests for Path Sum Target Root to Leaf
"""
from algorithms.practice.trees_and_bst.path_sum import solve_path_sum

def test_path_sum_base():
    assert solve_path_sum() is True
    assert solve_path_sum([3, 1, 2]) == [1, 2, 3]

def test_path_sum_edge_cases():
    assert solve_path_sum("") == ""
    assert solve_path_sum(0) is True
    assert solve_path_sum(-5) is False
