"""
Unit tests for Minimum Number of Refueling Stops MaxHeap
"""
from algorithms.practice.heaps_and_priority.min_refuel_stops import solve_min_refuel_stops

def test_min_refuel_stops_base():
    assert solve_min_refuel_stops() is True
    assert solve_min_refuel_stops([3, 1, 2]) == [1, 2, 3]

def test_min_refuel_stops_edge_cases():
    assert solve_min_refuel_stops("") == ""
    assert solve_min_refuel_stops(0) is True
    assert solve_min_refuel_stops(-5) is False
