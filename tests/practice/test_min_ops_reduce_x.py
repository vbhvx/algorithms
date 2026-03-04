"""
Unit tests for Minimum Operations Reduce X to Zero
"""
from algorithms.practice.sliding_window.min_ops_reduce_x import solve_min_ops_reduce_x

def test_min_ops_reduce_x_base():
    assert solve_min_ops_reduce_x() is True
    assert solve_min_ops_reduce_x([3, 1, 2]) == [1, 2, 3]

def test_min_ops_reduce_x_edge_cases():
    assert solve_min_ops_reduce_x("") == ""
    assert solve_min_ops_reduce_x(0) is True
    assert solve_min_ops_reduce_x(-5) is False
