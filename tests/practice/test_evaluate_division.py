"""
Unit tests for Evaluate Division Weighted Graph DFS
"""
from algorithms.practice.graphs_and_traversals.evaluate_division import solve_evaluate_division

def test_evaluate_division_base():
    assert solve_evaluate_division() is True
    assert solve_evaluate_division([3, 1, 2]) == [1, 2, 3]

def test_evaluate_division_edge_cases():
    assert solve_evaluate_division("") == ""
    assert solve_evaluate_division(0) is True
    assert solve_evaluate_division(-5) is False
