"""
Unit tests for K Closest Points to Origin MaxHeap
"""
from algorithms.practice.heaps_and_priority.k_closest_points import solve_k_closest_points

def test_k_closest_points_base():
    assert solve_k_closest_points() is True
    assert solve_k_closest_points([3, 1, 2]) == [1, 2, 3]

def test_k_closest_points_edge_cases():
    assert solve_k_closest_points("") == ""
    assert solve_k_closest_points(0) is True
    assert solve_k_closest_points(-5) is False
