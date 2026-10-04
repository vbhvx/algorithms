"""
Unit tests for Minimum Falling Path Sum II Running Two Mins
"""
from algorithms.practice.dynamic_programming_2d.min_falling_path_ii import solve_min_falling_path_ii

def test_min_falling_path_ii_base():
    assert solve_min_falling_path_ii() is True
    assert solve_min_falling_path_ii([3, 1, 2]) == [1, 2, 3]

def test_min_falling_path_ii_edge_cases():
    assert solve_min_falling_path_ii("") == ""
    assert solve_min_falling_path_ii(0) is True
    assert solve_min_falling_path_ii(-5) is False
