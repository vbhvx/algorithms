"""
Unit tests for Project Selection Problem Profit Maximization
"""
from algorithms.practice.network_flow_matching.project_selection_flow import solve_project_selection_flow

def test_project_selection_flow_base():
    assert solve_project_selection_flow() is True
    assert solve_project_selection_flow([3, 1, 2]) == [1, 2, 3]

def test_project_selection_flow_edge_cases():
    assert solve_project_selection_flow("") == ""
    assert solve_project_selection_flow(0) is True
    assert solve_project_selection_flow(-5) is False
