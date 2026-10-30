"""
Unit tests for Data Stream as Disjoint Intervals BST
"""
from algorithms.practice.intervals_scheduling.data_stream_intervals import solve_data_stream_intervals

def test_data_stream_intervals_base():
    assert solve_data_stream_intervals() is True
    assert solve_data_stream_intervals([3, 1, 2]) == [1, 2, 3]

def test_data_stream_intervals_edge_cases():
    assert solve_data_stream_intervals("") == ""
    assert solve_data_stream_intervals(0) is True
    assert solve_data_stream_intervals(-5) is False
