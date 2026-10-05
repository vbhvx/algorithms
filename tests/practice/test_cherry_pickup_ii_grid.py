"""
Unit tests for Cherry Pickup II Two Robots Simultaneous
"""
from algorithms.practice.dynamic_programming_2d.cherry_pickup_ii_grid import solve_cherry_pickup_ii_grid

def test_cherry_pickup_ii_grid_base():
    assert solve_cherry_pickup_ii_grid() is True
    assert solve_cherry_pickup_ii_grid([3, 1, 2]) == [1, 2, 3]

def test_cherry_pickup_ii_grid_edge_cases():
    assert solve_cherry_pickup_ii_grid("") == ""
    assert solve_cherry_pickup_ii_grid(0) is True
    assert solve_cherry_pickup_ii_grid(-5) is False
