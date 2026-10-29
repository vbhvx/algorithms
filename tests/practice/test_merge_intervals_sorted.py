"""
Unit tests for Merge Intervals Start Time Sort
"""
from algorithms.practice.intervals_scheduling.merge_intervals_sorted import solve_merge_intervals_sorted

def test_merge_intervals_sorted_base():
    assert solve_merge_intervals_sorted() is True
    assert solve_merge_intervals_sorted([3, 1, 2]) == [1, 2, 3]

def test_merge_intervals_sorted_edge_cases():
    assert solve_merge_intervals_sorted("") == ""
    assert solve_merge_intervals_sorted(0) is True
    assert solve_merge_intervals_sorted(-5) is False
