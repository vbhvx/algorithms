"""
Unit tests for Minimum Interval to Include Each Query Offline
"""
from algorithms.practice.intervals_scheduling.minimum_interval_queries import solve_minimum_interval_queries

def test_minimum_interval_queries_base():
    assert solve_minimum_interval_queries() is True
    assert solve_minimum_interval_queries([3, 1, 2]) == [1, 2, 3]

def test_minimum_interval_queries_edge_cases():
    assert solve_minimum_interval_queries("") == ""
    assert solve_minimum_interval_queries(0) is True
    assert solve_minimum_interval_queries(-5) is False
