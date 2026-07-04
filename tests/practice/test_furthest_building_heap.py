"""
Unit tests for Furthest Building You Can Reach MinHeap
"""
from algorithms.practice.heaps_and_priority.furthest_building_heap import solve_furthest_building_heap

def test_furthest_building_heap_base():
    assert solve_furthest_building_heap() is True
    assert solve_furthest_building_heap([3, 1, 2]) == [1, 2, 3]

def test_furthest_building_heap_edge_cases():
    assert solve_furthest_building_heap("") == ""
    assert solve_furthest_building_heap(0) is True
    assert solve_furthest_building_heap(-5) is False
