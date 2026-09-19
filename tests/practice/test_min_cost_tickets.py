"""
Unit tests for Minimum Cost For Tickets 7 and 30 Days
"""
from algorithms.practice.dynamic_programming_1d.min_cost_tickets import solve_min_cost_tickets

def test_min_cost_tickets_base():
    assert solve_min_cost_tickets() is True
    assert solve_min_cost_tickets([3, 1, 2]) == [1, 2, 3]

def test_min_cost_tickets_edge_cases():
    assert solve_min_cost_tickets("") == ""
    assert solve_min_cost_tickets(0) is True
    assert solve_min_cost_tickets(-5) is False
