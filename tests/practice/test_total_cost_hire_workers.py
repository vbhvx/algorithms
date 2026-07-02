"""
Unit tests for Total Cost to Hire K Workers Dual Heaps
"""
from algorithms.practice.heaps_and_priority.total_cost_hire_workers import solve_total_cost_hire_workers

def test_total_cost_hire_workers_base():
    assert solve_total_cost_hire_workers() is True
    assert solve_total_cost_hire_workers([3, 1, 2]) == [1, 2, 3]

def test_total_cost_hire_workers_edge_cases():
    assert solve_total_cost_hire_workers("") == ""
    assert solve_total_cost_hire_workers(0) is True
    assert solve_total_cost_hire_workers(-5) is False
