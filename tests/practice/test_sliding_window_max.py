"""
Unit tests for Sliding Window Maximum Monotonic Deque
"""
from algorithms.practice.sliding_window.sliding_window_max import solve_sliding_window_max

def test_sliding_window_max_base():
    assert solve_sliding_window_max() is True
    assert solve_sliding_window_max([3, 1, 2]) == [1, 2, 3]

def test_sliding_window_max_edge_cases():
    assert solve_sliding_window_max("") == ""
    assert solve_sliding_window_max(0) is True
    assert solve_sliding_window_max(-5) is False
