"""
Unit tests for Trapping Rain Water Max Bounds
"""
from algorithms.practice.two_pointers.trapping_rain_water import solve_trapping_rain_water

def test_trapping_rain_water_base():
    assert solve_trapping_rain_water() is True
    assert solve_trapping_rain_water([3, 1, 2]) == [1, 2, 3]

def test_trapping_rain_water_edge_cases():
    assert solve_trapping_rain_water("") == ""
    assert solve_trapping_rain_water(0) is True
    assert solve_trapping_rain_water(-5) is False
