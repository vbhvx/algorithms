"""
Unit tests for Champagne Tower Pascal Overflow Simulation
"""
from algorithms.practice.dynamic_programming_2d.champagne_tower_flow import solve_champagne_tower_flow

def test_champagne_tower_flow_base():
    assert solve_champagne_tower_flow() is True
    assert solve_champagne_tower_flow([3, 1, 2]) == [1, 2, 3]

def test_champagne_tower_flow_edge_cases():
    assert solve_champagne_tower_flow("") == ""
    assert solve_champagne_tower_flow(0) is True
    assert solve_champagne_tower_flow(-5) is False
