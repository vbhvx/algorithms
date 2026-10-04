"""
Unit tests for Minimum Falling Path Sum In-Place Row
"""
from algorithms.practice.dynamic_programming_2d.min_falling_path_sum import solve_min_falling_path_sum

def test_min_falling_path_sum_base():
    assert solve_min_falling_path_sum() is True
    assert solve_min_falling_path_sum([3, 1, 2]) == [1, 2, 3]

def test_min_falling_path_sum_edge_cases():
    assert solve_min_falling_path_sum("") == ""
    assert solve_min_falling_path_sum(0) is True
    assert solve_min_falling_path_sum(-5) is False
