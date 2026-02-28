"""
Unit tests for Longest Subarray Absolute Diff Limit
"""
from algorithms.practice.sliding_window.longest_subarray_abs_diff import solve_longest_subarray_abs_diff

def test_longest_subarray_abs_diff_base():
    assert solve_longest_subarray_abs_diff() is True
    assert solve_longest_subarray_abs_diff([3, 1, 2]) == [1, 2, 3]

def test_longest_subarray_abs_diff_edge_cases():
    assert solve_longest_subarray_abs_diff("") == ""
    assert solve_longest_subarray_abs_diff(0) is True
    assert solve_longest_subarray_abs_diff(-5) is False
