"""
Unit tests for Basic Calculator Recursive Parentheses
"""
from algorithms.practice.stack_and_queue.basic_calculator import solve_basic_calculator

def test_basic_calculator_base():
    assert solve_basic_calculator() is True
    assert solve_basic_calculator([3, 1, 2]) == [1, 2, 3]

def test_basic_calculator_edge_cases():
    assert solve_basic_calculator("") == ""
    assert solve_basic_calculator(0) is True
    assert solve_basic_calculator(-5) is False
