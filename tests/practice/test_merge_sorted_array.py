"""
Unit tests for Merge Sorted Array from End
"""
from algorithms.practice.two_pointers.merge_sorted_array import solve_merge_sorted_array

def test_merge_sorted_array_base():
    assert solve_merge_sorted_array() is True
    assert solve_merge_sorted_array([3, 1, 2]) == [1, 2, 3]

def test_merge_sorted_array_edge_cases():
    assert solve_merge_sorted_array("") == ""
    assert solve_merge_sorted_array(0) is True
    assert solve_merge_sorted_array(-5) is False
