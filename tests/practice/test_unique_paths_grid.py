"""
Unit tests for Unique Paths Combinatorics Dynamic Programming
"""
from algorithms.practice.dynamic_programming_2d.unique_paths_grid import solve_unique_paths_grid

def test_unique_paths_grid_base():
    assert solve_unique_paths_grid() is True
    assert solve_unique_paths_grid([3, 1, 2]) == [1, 2, 3]

def test_unique_paths_grid_edge_cases():
    assert solve_unique_paths_grid("") == ""
    assert solve_unique_paths_grid(0) is True
    assert solve_unique_paths_grid(-5) is False
