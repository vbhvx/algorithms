"""
Unit tests for Brick Wall Minimum Cross Cuts
"""
from algorithms.practice.arrays_and_hashing.brick_wall import solve_brick_wall

def test_brick_wall_base():
    assert solve_brick_wall() is True
    assert solve_brick_wall([3, 1, 2]) == [1, 2, 3]

def test_brick_wall_edge_cases():
    assert solve_brick_wall("") == ""
    assert solve_brick_wall(0) is True
    assert solve_brick_wall(-5) is False
