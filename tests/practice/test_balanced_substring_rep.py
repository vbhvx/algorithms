"""
Unit tests for Replace Substring Balanced String
"""
from algorithms.practice.sliding_window.balanced_substring_rep import solve_balanced_substring_rep

def test_balanced_substring_rep_base():
    assert solve_balanced_substring_rep() is True
    assert solve_balanced_substring_rep([3, 1, 2]) == [1, 2, 3]

def test_balanced_substring_rep_edge_cases():
    assert solve_balanced_substring_rep("") == ""
    assert solve_balanced_substring_rep(0) is True
    assert solve_balanced_substring_rep(-5) is False
