"""
Unit tests for Sliding Window Median Heaps
"""
from algorithms.practice.sliding_window.sliding_window_median import solve_sliding_window_median

def test_sliding_window_median_base():
    assert solve_sliding_window_median() is True
    assert solve_sliding_window_median([3, 1, 2]) == [1, 2, 3]

def test_sliding_window_median_edge_cases():
    assert solve_sliding_window_median("") == ""
    assert solve_sliding_window_median(0) is True
    assert solve_sliding_window_median(-5) is False
