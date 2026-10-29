"""
Unit tests for Insert Interval Overlap Merging
"""
from algorithms.practice.intervals_scheduling.insert_interval_sorted import solve_insert_interval_sorted

def test_insert_interval_sorted_base():
    assert solve_insert_interval_sorted() is True
    assert solve_insert_interval_sorted([3, 1, 2]) == [1, 2, 3]

def test_insert_interval_sorted_edge_cases():
    assert solve_insert_interval_sorted("") == ""
    assert solve_insert_interval_sorted(0) is True
    assert solve_insert_interval_sorted(-5) is False
