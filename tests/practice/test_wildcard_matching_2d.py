"""
Unit tests for Wildcard Matching Question Mark Star
"""
from algorithms.practice.dynamic_programming_2d.wildcard_matching_2d import solve_wildcard_matching_2d

def test_wildcard_matching_2d_base():
    assert solve_wildcard_matching_2d() is True
    assert solve_wildcard_matching_2d([3, 1, 2]) == [1, 2, 3]

def test_wildcard_matching_2d_edge_cases():
    assert solve_wildcard_matching_2d("") == ""
    assert solve_wildcard_matching_2d(0) is True
    assert solve_wildcard_matching_2d(-5) is False
