"""
Unit tests for Gas Station Starting Point Tank Deficit
"""
from algorithms.practice.greedy_algorithms.gas_station_circular import solve_gas_station_circular

def test_gas_station_circular_base():
    assert solve_gas_station_circular() is True
    assert solve_gas_station_circular([3, 1, 2]) == [1, 2, 3]

def test_gas_station_circular_edge_cases():
    assert solve_gas_station_circular("") == ""
    assert solve_gas_station_circular(0) is True
    assert solve_gas_station_circular(-5) is False
