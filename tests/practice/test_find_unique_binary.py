"""
Unit tests for Find Unique Binary String Cantor Diagonal
"""
from algorithms.practice.backtracking.find_unique_binary import solve_find_unique_binary

def test_find_unique_binary_base():
    assert solve_find_unique_binary() is True
    assert solve_find_unique_binary([3, 1, 2]) == [1, 2, 3]

def test_find_unique_binary_edge_cases():
    assert solve_find_unique_binary("") == ""
    assert solve_find_unique_binary(0) is True
    assert solve_find_unique_binary(-5) is False
