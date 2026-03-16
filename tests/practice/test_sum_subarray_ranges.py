"""
Unit tests for Sum of Subarray Ranges Monotonic Pair
"""
from algorithms.practice.stack_and_queue.sum_subarray_ranges import solve_sum_subarray_ranges

def test_sum_subarray_ranges_base():
    assert solve_sum_subarray_ranges() is True
    assert solve_sum_subarray_ranges([3, 1, 2]) == [1, 2, 3]

def test_sum_subarray_ranges_edge_cases():
    assert solve_sum_subarray_ranges("") == ""
    assert solve_sum_subarray_ranges(0) is True
    assert solve_sum_subarray_ranges(-5) is False
