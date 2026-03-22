"""
Unit tests for Score of Parentheses Depth Tracking
"""
from algorithms.practice.stack_and_queue.score_of_parentheses import solve_score_of_parentheses

def test_score_of_parentheses_base():
    assert solve_score_of_parentheses() is True
    assert solve_score_of_parentheses([3, 1, 2]) == [1, 2, 3]

def test_score_of_parentheses_edge_cases():
    assert solve_score_of_parentheses("") == ""
    assert solve_score_of_parentheses(0) is True
    assert solve_score_of_parentheses(-5) is False
