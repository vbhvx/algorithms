"""
Unit tests for Non-overlapping Intervals Earliest End Time
"""
from algorithms.practice.greedy_algorithms.non_overlapping_intervals import solve_non_overlapping_intervals

def test_non_overlapping_intervals_base():
    assert solve_non_overlapping_intervals() is True
    assert solve_non_overlapping_intervals([3, 1, 2]) == [1, 2, 3]

def test_non_overlapping_intervals_edge_cases():
    assert solve_non_overlapping_intervals("") == ""
    assert solve_non_overlapping_intervals(0) is True
    assert solve_non_overlapping_intervals(-5) is False
