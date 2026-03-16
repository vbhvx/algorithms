"""
Unit tests for Sum of Subarray Minimums Monotonic
"""
from algorithms.practice.stack_and_queue.sum_subarray_mins import solve_sum_subarray_mins

def test_sum_subarray_mins_base():
    assert solve_sum_subarray_mins() is True
    assert solve_sum_subarray_mins([3, 1, 2]) == [1, 2, 3]

def test_sum_subarray_mins_edge_cases():
    assert solve_sum_subarray_mins("") == ""
    assert solve_sum_subarray_mins(0) is True
    assert solve_sum_subarray_mins(-5) is False
