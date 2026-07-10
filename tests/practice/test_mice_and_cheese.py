"""
Unit tests for Mice and Cheese Greedy MaxHeap Difference
"""
from algorithms.practice.heaps_and_priority.mice_and_cheese import solve_mice_and_cheese

def test_mice_and_cheese_base():
    assert solve_mice_and_cheese() is True
    assert solve_mice_and_cheese([3, 1, 2]) == [1, 2, 3]

def test_mice_and_cheese_edge_cases():
    assert solve_mice_and_cheese("") == ""
    assert solve_mice_and_cheese(0) is True
    assert solve_mice_and_cheese(-5) is False
