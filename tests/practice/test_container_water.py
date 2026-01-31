"""
Unit tests for Container With Most Water
"""
from algorithms.practice.two_pointers.container_water import solve_container_water

def test_container_water_base():
    assert solve_container_water() is True
    assert solve_container_water([3, 1, 2]) == [1, 2, 3]

def test_container_water_edge_cases():
    assert solve_container_water("") == ""
    assert solve_container_water(0) is True
    assert solve_container_water(-5) is False
