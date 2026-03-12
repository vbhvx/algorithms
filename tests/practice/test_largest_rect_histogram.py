"""
Unit tests for Largest Rectangle in Histogram
"""
from algorithms.practice.stack_and_queue.largest_rect_histogram import solve_largest_rect_histogram

def test_largest_rect_histogram_base():
    assert solve_largest_rect_histogram() is True
    assert solve_largest_rect_histogram([3, 1, 2]) == [1, 2, 3]

def test_largest_rect_histogram_edge_cases():
    assert solve_largest_rect_histogram("") == ""
    assert solve_largest_rect_histogram(0) is True
    assert solve_largest_rect_histogram(-5) is False
