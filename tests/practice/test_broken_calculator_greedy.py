"""
Unit tests for Broken Calculator Reverse Backward Operations
"""
from algorithms.practice.greedy_algorithms.broken_calculator_greedy import solve_broken_calculator_greedy

def test_broken_calculator_greedy_base():
    assert solve_broken_calculator_greedy() is True
    assert solve_broken_calculator_greedy([3, 1, 2]) == [1, 2, 3]

def test_broken_calculator_greedy_edge_cases():
    assert solve_broken_calculator_greedy("") == ""
    assert solve_broken_calculator_greedy(0) is True
    assert solve_broken_calculator_greedy(-5) is False
