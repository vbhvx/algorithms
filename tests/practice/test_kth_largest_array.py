"""
Unit tests for Kth Largest Element in Array QuickSelect MinHeap
"""
from algorithms.practice.heaps_and_priority.kth_largest_array import solve_kth_largest_array

def test_kth_largest_array_base():
    assert solve_kth_largest_array() is True
    assert solve_kth_largest_array([3, 1, 2]) == [1, 2, 3]

def test_kth_largest_array_edge_cases():
    assert solve_kth_largest_array("") == ""
    assert solve_kth_largest_array(0) is True
    assert solve_kth_largest_array(-5) is False
