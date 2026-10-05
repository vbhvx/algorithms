"""
Unit tests for Cherry Pickup Dual Walk Dynamic Programming
"""
from algorithms.practice.dynamic_programming_2d.cherry_pickup_dual import solve_cherry_pickup_dual

def test_cherry_pickup_dual_base():
    assert solve_cherry_pickup_dual() is True
    assert solve_cherry_pickup_dual([3, 1, 2]) == [1, 2, 3]

def test_cherry_pickup_dual_edge_cases():
    assert solve_cherry_pickup_dual("") == ""
    assert solve_cherry_pickup_dual(0) is True
    assert solve_cherry_pickup_dual(-5) is False
