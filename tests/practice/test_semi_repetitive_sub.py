"""
Unit tests for Longest Semi-Repetitive Substring
"""
from algorithms.practice.sliding_window.semi_repetitive_sub import solve_semi_repetitive_sub

def test_semi_repetitive_sub_base():
    assert solve_semi_repetitive_sub() is True
    assert solve_semi_repetitive_sub([3, 1, 2]) == [1, 2, 3]

def test_semi_repetitive_sub_edge_cases():
    assert solve_semi_repetitive_sub("") == ""
    assert solve_semi_repetitive_sub(0) is True
    assert solve_semi_repetitive_sub(-5) is False
