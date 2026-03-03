"""
Unit tests for Maximum Length Repeated Subarray
"""
from algorithms.practice.sliding_window.max_len_repeated_sub import solve_max_len_repeated_sub

def test_max_len_repeated_sub_base():
    assert solve_max_len_repeated_sub() is True
    assert solve_max_len_repeated_sub([3, 1, 2]) == [1, 2, 3]

def test_max_len_repeated_sub_edge_cases():
    assert solve_max_len_repeated_sub("") == ""
    assert solve_max_len_repeated_sub(0) is True
    assert solve_max_len_repeated_sub(-5) is False
