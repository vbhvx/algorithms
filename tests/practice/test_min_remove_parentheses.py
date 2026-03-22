"""
Unit tests for Minimum Remove to Make Valid Parentheses
"""
from algorithms.practice.stack_and_queue.min_remove_parentheses import solve_min_remove_parentheses

def test_min_remove_parentheses_base():
    assert solve_min_remove_parentheses() is True
    assert solve_min_remove_parentheses([3, 1, 2]) == [1, 2, 3]

def test_min_remove_parentheses_edge_cases():
    assert solve_min_remove_parentheses("") == ""
    assert solve_min_remove_parentheses(0) is True
    assert solve_min_remove_parentheses(-5) is False
