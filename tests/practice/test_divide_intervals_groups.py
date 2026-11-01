"""
Unit tests for Divide Intervals Into Minimum Number of Groups
"""
from algorithms.practice.intervals_scheduling.divide_intervals_groups import solve_divide_intervals_groups

def test_divide_intervals_groups_base():
    assert solve_divide_intervals_groups() is True
    assert solve_divide_intervals_groups([3, 1, 2]) == [1, 2, 3]

def test_divide_intervals_groups_edge_cases():
    assert solve_divide_intervals_groups("") == ""
    assert solve_divide_intervals_groups(0) is True
    assert solve_divide_intervals_groups(-5) is False
