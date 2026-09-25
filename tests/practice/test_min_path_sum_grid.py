"""
Unit tests for Minimum Path Sum Matrix In-Place
"""
from algorithms.practice.dynamic_programming_2d.min_path_sum_grid import solve_min_path_sum_grid

def test_min_path_sum_grid_base():
    assert solve_min_path_sum_grid() is True
    assert solve_min_path_sum_grid([3, 1, 2]) == [1, 2, 3]

def test_min_path_sum_grid_edge_cases():
    assert solve_min_path_sum_grid("") == ""
    assert solve_min_path_sum_grid(0) is True
    assert solve_min_path_sum_grid(-5) is False
