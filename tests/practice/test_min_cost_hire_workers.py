"""
Unit tests for Minimum Cost to Hire K Workers Ratio Heap
"""
from algorithms.practice.heaps_and_priority.min_cost_hire_workers import solve_min_cost_hire_workers

def test_min_cost_hire_workers_base():
    assert solve_min_cost_hire_workers() is True
    assert solve_min_cost_hire_workers([3, 1, 2]) == [1, 2, 3]

def test_min_cost_hire_workers_edge_cases():
    assert solve_min_cost_hire_workers("") == ""
    assert solve_min_cost_hire_workers(0) is True
    assert solve_min_cost_hire_workers(-5) is False
