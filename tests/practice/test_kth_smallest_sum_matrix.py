"""
Unit tests for Kth Smallest Sum of Matrix Rows MinHeap
"""
from algorithms.practice.heaps_and_priority.kth_smallest_sum_matrix import solve_kth_smallest_sum_matrix

def test_kth_smallest_sum_matrix_base():
    assert solve_kth_smallest_sum_matrix() is True
    assert solve_kth_smallest_sum_matrix([3, 1, 2]) == [1, 2, 3]

def test_kth_smallest_sum_matrix_edge_cases():
    assert solve_kth_smallest_sum_matrix("") == ""
    assert solve_kth_smallest_sum_matrix(0) is True
    assert solve_kth_smallest_sum_matrix(-5) is False
