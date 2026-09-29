"""
Unit tests for Regular Expression Matching Wildcard Star
"""
from algorithms.practice.dynamic_programming_2d.regex_matching_dp import solve_regex_matching_dp

def test_regex_matching_dp_base():
    assert solve_regex_matching_dp() is True
    assert solve_regex_matching_dp([3, 1, 2]) == [1, 2, 3]

def test_regex_matching_dp_edge_cases():
    assert solve_regex_matching_dp("") == ""
    assert solve_regex_matching_dp(0) is True
    assert solve_regex_matching_dp(-5) is False
