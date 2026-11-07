"""
Unit tests for Maximum Beauty of an Array After Operations
"""
from algorithms.practice.intervals_scheduling.maximum_beauty_intervals import solve_maximum_beauty_intervals

def test_maximum_beauty_intervals_base():
    assert solve_maximum_beauty_intervals() is True
    assert solve_maximum_beauty_intervals([3, 1, 2]) == [1, 2, 3]

def test_maximum_beauty_intervals_edge_cases():
    assert solve_maximum_beauty_intervals("") == ""
    assert solve_maximum_beauty_intervals(0) is True
    assert solve_maximum_beauty_intervals(-5) is False
