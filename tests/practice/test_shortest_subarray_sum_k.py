"""
Unit tests for Shortest Subarray Sum at Least K
"""
from algorithms.practice.sliding_window.shortest_subarray_sum_k import solve_shortest_subarray_sum_k

def test_shortest_subarray_sum_k_base():
    assert solve_shortest_subarray_sum_k() is True
    assert solve_shortest_subarray_sum_k([3, 1, 2]) == [1, 2, 3]

def test_shortest_subarray_sum_k_edge_cases():
    assert solve_shortest_subarray_sum_k("") == ""
    assert solve_shortest_subarray_sum_k(0) is True
    assert solve_shortest_subarray_sum_k(-5) is False
