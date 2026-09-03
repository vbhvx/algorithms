"""
Unit tests for Circulation with Demands Lower Upper Bounds
"""
from algorithms.practice.network_flow_matching.circulation_with_demands import solve_circulation_with_demands

def test_circulation_with_demands_base():
    assert solve_circulation_with_demands() is True
    assert solve_circulation_with_demands([3, 1, 2]) == [1, 2, 3]

def test_circulation_with_demands_edge_cases():
    assert solve_circulation_with_demands("") == ""
    assert solve_circulation_with_demands(0) is True
    assert solve_circulation_with_demands(-5) is False
