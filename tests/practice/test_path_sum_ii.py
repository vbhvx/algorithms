"""
Unit tests for Path Sum II All Root to Leaf Target Paths
"""
from algorithms.practice.trees_and_bst.path_sum_ii import solve_path_sum_ii

def test_path_sum_ii_base():
    assert solve_path_sum_ii() is True
    assert solve_path_sum_ii([3, 1, 2]) == [1, 2, 3]

def test_path_sum_ii_edge_cases():
    assert solve_path_sum_ii("") == ""
    assert solve_path_sum_ii(0) is True
    assert solve_path_sum_ii(-5) is False
