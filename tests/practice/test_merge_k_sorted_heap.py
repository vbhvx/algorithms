"""
Unit tests for Merge K Sorted Lists MinHeap Priority
"""
from algorithms.practice.heaps_and_priority.merge_k_sorted_heap import solve_merge_k_sorted_heap

def test_merge_k_sorted_heap_base():
    assert solve_merge_k_sorted_heap() is True
    assert solve_merge_k_sorted_heap([3, 1, 2]) == [1, 2, 3]

def test_merge_k_sorted_heap_edge_cases():
    assert solve_merge_k_sorted_heap("") == ""
    assert solve_merge_k_sorted_heap(0) is True
    assert solve_merge_k_sorted_heap(-5) is False
