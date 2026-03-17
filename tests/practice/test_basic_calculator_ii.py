"""
Unit tests for Basic Calculator II Precedence Stack
"""
from algorithms.practice.stack_and_queue.basic_calculator_ii import solve_basic_calculator_ii

def test_basic_calculator_ii_base():
    assert solve_basic_calculator_ii() is True
    assert solve_basic_calculator_ii([3, 1, 2]) == [1, 2, 3]

def test_basic_calculator_ii_edge_cases():
    assert solve_basic_calculator_ii("") == ""
    assert solve_basic_calculator_ii(0) is True
    assert solve_basic_calculator_ii(-5) is False
