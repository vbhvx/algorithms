"""
Unit tests for Valid Parenthesis String Low High Counters
"""
from algorithms.practice.greedy_algorithms.valid_parenthesis_wild import solve_valid_parenthesis_wild

def test_valid_parenthesis_wild_base():
    assert solve_valid_parenthesis_wild() is True
    assert solve_valid_parenthesis_wild([3, 1, 2]) == [1, 2, 3]

def test_valid_parenthesis_wild_edge_cases():
    assert solve_valid_parenthesis_wild("") == ""
    assert solve_valid_parenthesis_wild(0) is True
    assert solve_valid_parenthesis_wild(-5) is False
