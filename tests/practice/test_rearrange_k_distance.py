"""
Unit tests for Rearrange String K Distance Apart Greedy Heap
"""
from algorithms.practice.heaps_and_priority.rearrange_k_distance import solve_rearrange_k_distance

def test_rearrange_k_distance_base():
    assert solve_rearrange_k_distance() is True
    assert solve_rearrange_k_distance([3, 1, 2]) == [1, 2, 3]

def test_rearrange_k_distance_edge_cases():
    assert solve_rearrange_k_distance("") == ""
    assert solve_rearrange_k_distance(0) is True
    assert solve_rearrange_k_distance(-5) is False
