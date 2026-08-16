"""
Unit tests for Path with Minimum Effort Binary Search Dijkstra
"""
from algorithms.practice.shortest_paths.path_minimum_effort import solve_path_minimum_effort

def test_path_minimum_effort_base():
    assert solve_path_minimum_effort() is True
    assert solve_path_minimum_effort([3, 1, 2]) == [1, 2, 3]

def test_path_minimum_effort_edge_cases():
    assert solve_path_minimum_effort("") == ""
    assert solve_path_minimum_effort(0) is True
    assert solve_path_minimum_effort(-5) is False
