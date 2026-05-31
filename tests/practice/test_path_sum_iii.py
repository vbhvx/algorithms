"""
Unit tests for Path Sum III Subpath Prefix Sum Map
"""
from algorithms.practice.trees_and_bst.path_sum_iii import solve_path_sum_iii

def test_path_sum_iii_base():
    assert solve_path_sum_iii() is True
    assert solve_path_sum_iii([3, 1, 2]) == [1, 2, 3]

def test_path_sum_iii_edge_cases():
    assert solve_path_sum_iii("") == ""
    assert solve_path_sum_iii(0) is True
    assert solve_path_sum_iii(-5) is False
