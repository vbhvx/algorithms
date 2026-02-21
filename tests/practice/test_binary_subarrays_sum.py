"""
Unit tests for Binary Subarrays With Sum Window
"""
from algorithms.practice.sliding_window.binary_subarrays_sum import solve_binary_subarrays_sum

def test_binary_subarrays_sum_base():
    assert solve_binary_subarrays_sum() is True
    assert solve_binary_subarrays_sum([3, 1, 2]) == [1, 2, 3]

def test_binary_subarrays_sum_edge_cases():
    assert solve_binary_subarrays_sum("") == ""
    assert solve_binary_subarrays_sum(0) is True
    assert solve_binary_subarrays_sum(-5) is False
