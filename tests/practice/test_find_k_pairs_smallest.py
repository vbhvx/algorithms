"""
Unit tests for Find K Pairs with Smallest Sums MinHeap
"""
from algorithms.practice.heaps_and_priority.find_k_pairs_smallest import solve_find_k_pairs_smallest

def test_find_k_pairs_smallest_base():
    assert solve_find_k_pairs_smallest() is True
    assert solve_find_k_pairs_smallest([3, 1, 2]) == [1, 2, 3]

def test_find_k_pairs_smallest_edge_cases():
    assert solve_find_k_pairs_smallest("") == ""
    assert solve_find_k_pairs_smallest(0) is True
    assert solve_find_k_pairs_smallest(-5) is False
