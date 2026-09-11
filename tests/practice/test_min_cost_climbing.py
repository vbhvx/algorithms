"""
Unit tests for Min Cost Climbing Stairs Recurrence
"""
from algorithms.practice.dynamic_programming_1d.min_cost_climbing import solve_min_cost_climbing

def test_min_cost_climbing_base():
    assert solve_min_cost_climbing() is True
    assert solve_min_cost_climbing([3, 1, 2]) == [1, 2, 3]

def test_min_cost_climbing_edge_cases():
    assert solve_min_cost_climbing("") == ""
    assert solve_min_cost_climbing(0) is True
    assert solve_min_cost_climbing(-5) is False
