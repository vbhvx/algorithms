"""
Unit tests for Expression Add Operators Precedence Backtrack
"""
from algorithms.practice.backtracking.expression_add_ops import solve_expression_add_ops

def test_expression_add_ops_base():
    assert solve_expression_add_ops() is True
    assert solve_expression_add_ops([3, 1, 2]) == [1, 2, 3]

def test_expression_add_ops_edge_cases():
    assert solve_expression_add_ops("") == ""
    assert solve_expression_add_ops(0) is True
    assert solve_expression_add_ops(-5) is False
