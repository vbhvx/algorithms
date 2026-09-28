"""
Unit tests for Burst Balloons Interval Dynamic Programming
"""
from algorithms.practice.dynamic_programming_2d.burst_balloons_interval import solve_burst_balloons_interval

def test_burst_balloons_interval_base():
    assert solve_burst_balloons_interval() is True
    assert solve_burst_balloons_interval([3, 1, 2]) == [1, 2, 3]

def test_burst_balloons_interval_edge_cases():
    assert solve_burst_balloons_interval("") == ""
    assert solve_burst_balloons_interval(0) is True
    assert solve_burst_balloons_interval(-5) is False
