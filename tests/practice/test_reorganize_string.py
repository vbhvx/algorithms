"""
Unit tests for Reorganize String MaxHeap Greedy Spacing
"""
from algorithms.practice.heaps_and_priority.reorganize_string import solve_reorganize_string

def test_reorganize_string_base():
    assert solve_reorganize_string() is True
    assert solve_reorganize_string([3, 1, 2]) == [1, 2, 3]

def test_reorganize_string_edge_cases():
    assert solve_reorganize_string("") == ""
    assert solve_reorganize_string(0) is True
    assert solve_reorganize_string(-5) is False
