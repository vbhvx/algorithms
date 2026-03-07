"""
Unit tests for Subarrays Max Element K Times
"""
from algorithms.practice.sliding_window.max_element_k_times import solve_max_element_k_times

def test_max_element_k_times_base():
    assert solve_max_element_k_times() is True
    assert solve_max_element_k_times([3, 1, 2]) == [1, 2, 3]

def test_max_element_k_times_edge_cases():
    assert solve_max_element_k_times("") == ""
    assert solve_max_element_k_times(0) is True
    assert solve_max_element_k_times(-5) is False
