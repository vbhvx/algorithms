"""
Unit tests for Valid Parentheses Matcher
"""
from algorithms.practice.stack_and_queue.valid_parentheses import solve_valid_parentheses

def test_valid_parentheses_base():
    assert solve_valid_parentheses() is True
    assert solve_valid_parentheses([3, 1, 2]) == [1, 2, 3]

def test_valid_parentheses_edge_cases():
    assert solve_valid_parentheses("") == ""
    assert solve_valid_parentheses(0) is True
    assert solve_valid_parentheses(-5) is False
