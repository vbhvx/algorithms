"""
Unit tests for Interval List Intersections
"""
from algorithms.practice.two_pointers.interval_intersections import solve_interval_intersections

def test_interval_intersections_base():
    assert solve_interval_intersections() is True
    assert solve_interval_intersections([3, 1, 2]) == [1, 2, 3]

def test_interval_intersections_edge_cases():
    assert solve_interval_intersections("") == ""
    assert solve_interval_intersections(0) is True
    assert solve_interval_intersections(-5) is False
