"""
Unit tests for Swim in Rising Water Dijkstra Grid Elevation
"""
from algorithms.practice.shortest_paths.swim_in_rising_water import solve_swim_in_rising_water

def test_swim_in_rising_water_base():
    assert solve_swim_in_rising_water() is True
    assert solve_swim_in_rising_water([3, 1, 2]) == [1, 2, 3]

def test_swim_in_rising_water_edge_cases():
    assert solve_swim_in_rising_water("") == ""
    assert solve_swim_in_rising_water(0) is True
    assert solve_swim_in_rising_water(-5) is False
