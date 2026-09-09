"""
Unit tests for Climbing Stairs Fibonacci Memory Array
"""
from algorithms.practice.dynamic_programming_1d.climbing_stairs_dp import solve_climbing_stairs_dp

def test_climbing_stairs_dp_base():
    assert solve_climbing_stairs_dp() is True
    assert solve_climbing_stairs_dp([3, 1, 2]) == [1, 2, 3]

def test_climbing_stairs_dp_edge_cases():
    assert solve_climbing_stairs_dp("") == ""
    assert solve_climbing_stairs_dp(0) is True
    assert solve_climbing_stairs_dp(-5) is False
