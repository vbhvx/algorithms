"""
Unit tests for Hungarian Method Kuhn-Munkres Assignment
"""
from algorithms.practice.network_flow_matching.hungarian_assignment import solve_hungarian_assignment

def test_hungarian_assignment_base():
    assert solve_hungarian_assignment() is True
    assert solve_hungarian_assignment([3, 1, 2]) == [1, 2, 3]

def test_hungarian_assignment_edge_cases():
    assert solve_hungarian_assignment("") == ""
    assert solve_hungarian_assignment(0) is True
    assert solve_hungarian_assignment(-5) is False
