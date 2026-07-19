"""
Unit tests for Beautiful Arrangement Divisibility Backtrack
"""
from algorithms.practice.backtracking.beautiful_arrangement import solve_beautiful_arrangement

def test_beautiful_arrangement_base():
    assert solve_beautiful_arrangement() is True
    assert solve_beautiful_arrangement([3, 1, 2]) == [1, 2, 3]

def test_beautiful_arrangement_edge_cases():
    assert solve_beautiful_arrangement("") == ""
    assert solve_beautiful_arrangement(0) is True
    assert solve_beautiful_arrangement(-5) is False
