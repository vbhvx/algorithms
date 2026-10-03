"""
Unit tests for Ones and Zeroes 2D Knapsack Capacity
"""
from algorithms.practice.dynamic_programming_2d.ones_and_zeroes_2d import solve_ones_and_zeroes_2d

def test_ones_and_zeroes_2d_base():
    assert solve_ones_and_zeroes_2d() is True
    assert solve_ones_and_zeroes_2d([3, 1, 2]) == [1, 2, 3]

def test_ones_and_zeroes_2d_edge_cases():
    assert solve_ones_and_zeroes_2d("") == ""
    assert solve_ones_and_zeroes_2d(0) is True
    assert solve_ones_and_zeroes_2d(-5) is False
