"""
Unit tests for Find Eventual Safe States Cycle Detection
"""
from algorithms.practice.graphs_and_traversals.find_eventual_safe import solve_find_eventual_safe

def test_find_eventual_safe_base():
    assert solve_find_eventual_safe() is True
    assert solve_find_eventual_safe([3, 1, 2]) == [1, 2, 3]

def test_find_eventual_safe_edge_cases():
    assert solve_find_eventual_safe("") == ""
    assert solve_find_eventual_safe(0) is True
    assert solve_find_eventual_safe(-5) is False
