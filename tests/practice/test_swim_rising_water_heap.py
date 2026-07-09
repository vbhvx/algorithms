"""
Unit tests for Swim in Rising Water Dijkstra Priority Queue
"""
from algorithms.practice.heaps_and_priority.swim_rising_water_heap import solve_swim_rising_water_heap

def test_swim_rising_water_heap_base():
    assert solve_swim_rising_water_heap() is True
    assert solve_swim_rising_water_heap([3, 1, 2]) == [1, 2, 3]

def test_swim_rising_water_heap_edge_cases():
    assert solve_swim_rising_water_heap("") == ""
    assert solve_swim_rising_water_heap(0) is True
    assert solve_swim_rising_water_heap(-5) is False
