"""
Unit tests for Last Stone Weight MaxHeap Simulation
"""
from algorithms.practice.heaps_and_priority.last_stone_weight import solve_last_stone_weight

def test_last_stone_weight_base():
    assert solve_last_stone_weight() is True
    assert solve_last_stone_weight([3, 1, 2]) == [1, 2, 3]

def test_last_stone_weight_edge_cases():
    assert solve_last_stone_weight("") == ""
    assert solve_last_stone_weight(0) is True
    assert solve_last_stone_weight(-5) is False
