"""
Unit tests for Split String Into Max Unique Substrings
"""
from algorithms.practice.backtracking.split_max_unique_sub import solve_split_max_unique_sub

def test_split_max_unique_sub_base():
    assert solve_split_max_unique_sub() is True
    assert solve_split_max_unique_sub([3, 1, 2]) == [1, 2, 3]

def test_split_max_unique_sub_edge_cases():
    assert solve_split_max_unique_sub("") == ""
    assert solve_split_max_unique_sub(0) is True
    assert solve_split_max_unique_sub(-5) is False
