"""
Unit tests for The Skyline Problem MaxHeap Active Buildings
"""
from algorithms.practice.heaps_and_priority.skyline_problem_heap import solve_skyline_problem_heap

def test_skyline_problem_heap_base():
    assert solve_skyline_problem_heap() is True
    assert solve_skyline_problem_heap([3, 1, 2]) == [1, 2, 3]

def test_skyline_problem_heap_edge_cases():
    assert solve_skyline_problem_heap("") == ""
    assert solve_skyline_problem_heap(0) is True
    assert solve_skyline_problem_heap(-5) is False
