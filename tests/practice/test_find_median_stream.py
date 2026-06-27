"""
Unit tests for Find Median from Data Stream Dual Heaps
"""
from algorithms.practice.heaps_and_priority.find_median_stream import solve_find_median_stream

def test_find_median_stream_base():
    assert solve_find_median_stream() is True
    assert solve_find_median_stream([3, 1, 2]) == [1, 2, 3]

def test_find_median_stream_edge_cases():
    assert solve_find_median_stream("") == ""
    assert solve_find_median_stream(0) is True
    assert solve_find_median_stream(-5) is False
