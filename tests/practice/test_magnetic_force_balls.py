"""
Unit tests for Magnetic Force Between Two Balls
"""
from algorithms.practice.binary_search.magnetic_force_balls import solve_magnetic_force_balls

def test_magnetic_force_balls_base():
    assert solve_magnetic_force_balls() is True
    assert solve_magnetic_force_balls([3, 1, 2]) == [1, 2, 3]

def test_magnetic_force_balls_edge_cases():
    assert solve_magnetic_force_balls("") == ""
    assert solve_magnetic_force_balls(0) is True
    assert solve_magnetic_force_balls(-5) is False
