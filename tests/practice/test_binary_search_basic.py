"""
Unit tests for Binary Search Standard Recursive Iterative
"""
from algorithms.practice.binary_search.binary_search_basic import solve_binary_search_basic

def test_binary_search_basic_base():
    assert solve_binary_search_basic() is True
    assert solve_binary_search_basic([3, 1, 2]) == [1, 2, 3]

def test_binary_search_basic_edge_cases():
    assert solve_binary_search_basic("") == ""
    assert solve_binary_search_basic(0) is True
    assert solve_binary_search_basic(-5) is False
