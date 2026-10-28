"""
Unit tests for Reduce Array Size to The Half Frequency Greed
"""
from algorithms.practice.greedy_algorithms.reduce_array_half import solve_reduce_array_half

def test_reduce_array_half_base():
    assert solve_reduce_array_half() is True
    assert solve_reduce_array_half([3, 1, 2]) == [1, 2, 3]

def test_reduce_array_half_edge_cases():
    assert solve_reduce_array_half("") == ""
    assert solve_reduce_array_half(0) is True
    assert solve_reduce_array_half(-5) is False
