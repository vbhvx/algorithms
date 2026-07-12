"""
Unit tests for Minimum Interval to Include Each Query MinHeap
"""
from algorithms.practice.heaps_and_priority.minimum_interval_query import solve_minimum_interval_query

def test_minimum_interval_query_base():
    assert solve_minimum_interval_query() is True
    assert solve_minimum_interval_query([3, 1, 2]) == [1, 2, 3]

def test_minimum_interval_query_edge_cases():
    assert solve_minimum_interval_query("") == ""
    assert solve_minimum_interval_query(0) is True
    assert solve_minimum_interval_query(-5) is False
