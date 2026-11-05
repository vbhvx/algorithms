"""
Unit tests for Remove Covered Intervals Sort Left Right
"""
from algorithms.practice.intervals_scheduling.remove_covered_intervals import solve_remove_covered_intervals

def test_remove_covered_intervals_base():
    assert solve_remove_covered_intervals() is True
    assert solve_remove_covered_intervals([3, 1, 2]) == [1, 2, 3]

def test_remove_covered_intervals_edge_cases():
    assert solve_remove_covered_intervals("") == ""
    assert solve_remove_covered_intervals(0) is True
    assert solve_remove_covered_intervals(-5) is False
