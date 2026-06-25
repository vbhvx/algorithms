"""
Unit tests for Kth Largest Element in a Stream MinHeap
"""
from algorithms.practice.heaps_and_priority.kth_largest_stream import solve_kth_largest_stream

def test_kth_largest_stream_base():
    assert solve_kth_largest_stream() is True
    assert solve_kth_largest_stream([3, 1, 2]) == [1, 2, 3]

def test_kth_largest_stream_edge_cases():
    assert solve_kth_largest_stream("") == ""
    assert solve_kth_largest_stream(0) is True
    assert solve_kth_largest_stream(-5) is False
