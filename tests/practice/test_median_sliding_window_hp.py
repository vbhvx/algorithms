"""
Unit tests for Median Sliding Window Dual Heaps Lazy Deletion
"""
from algorithms.practice.heaps_and_priority.median_sliding_window_hp import solve_median_sliding_window_hp

def test_median_sliding_window_hp_base():
    assert solve_median_sliding_window_hp() is True
    assert solve_median_sliding_window_hp([3, 1, 2]) == [1, 2, 3]

def test_median_sliding_window_hp_edge_cases():
    assert solve_median_sliding_window_hp("") == ""
    assert solve_median_sliding_window_hp(0) is True
    assert solve_median_sliding_window_hp(-5) is False
