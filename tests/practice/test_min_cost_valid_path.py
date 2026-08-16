"""
Unit tests for Minimum Cost to Make at Least One Valid Path 0-1 BFS
"""
from algorithms.practice.shortest_paths.min_cost_valid_path import solve_min_cost_valid_path

def test_min_cost_valid_path_base():
    assert solve_min_cost_valid_path() is True
    assert solve_min_cost_valid_path([3, 1, 2]) == [1, 2, 3]

def test_min_cost_valid_path_edge_cases():
    assert solve_min_cost_valid_path("") == ""
    assert solve_min_cost_valid_path(0) is True
    assert solve_min_cost_valid_path(-5) is False
