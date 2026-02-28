"""
Unit tests for Equal Substrings Within Budget
"""
from algorithms.practice.sliding_window.equal_substrings_budget import solve_equal_substrings_budget

def test_equal_substrings_budget_base():
    assert solve_equal_substrings_budget() is True
    assert solve_equal_substrings_budget([3, 1, 2]) == [1, 2, 3]

def test_equal_substrings_budget_edge_cases():
    assert solve_equal_substrings_budget("") == ""
    assert solve_equal_substrings_budget(0) is True
    assert solve_equal_substrings_budget(-5) is False
