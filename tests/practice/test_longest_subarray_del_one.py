"""
Unit tests for Longest Subarray of 1s Delete One
"""
from algorithms.practice.sliding_window.longest_subarray_del_one import solve_longest_subarray_del_one

def test_longest_subarray_del_one_base():
    assert solve_longest_subarray_del_one() is True
    assert solve_longest_subarray_del_one([3, 1, 2]) == [1, 2, 3]

def test_longest_subarray_del_one_edge_cases():
    assert solve_longest_subarray_del_one("") == ""
    assert solve_longest_subarray_del_one(0) is True
    assert solve_longest_subarray_del_one(-5) is False
