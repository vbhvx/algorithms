"""
Unit tests for Path with Maximum Gold DFS Matrix Visited
"""
from algorithms.practice.backtracking.path_maximum_gold import solve_path_maximum_gold

def test_path_maximum_gold_base():
    assert solve_path_maximum_gold() is True
    assert solve_path_maximum_gold([3, 1, 2]) == [1, 2, 3]

def test_path_maximum_gold_edge_cases():
    assert solve_path_maximum_gold("") == ""
    assert solve_path_maximum_gold(0) is True
    assert solve_path_maximum_gold(-5) is False
