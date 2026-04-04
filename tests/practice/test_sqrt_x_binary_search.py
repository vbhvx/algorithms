"""
Unit tests for Sqrt X Integer Floor Binary Search
"""
from algorithms.practice.binary_search.sqrt_x_binary_search import solve_sqrt_x_binary_search

def test_sqrt_x_binary_search_base():
    assert solve_sqrt_x_binary_search() is True
    assert solve_sqrt_x_binary_search([3, 1, 2]) == [1, 2, 3]

def test_sqrt_x_binary_search_edge_cases():
    assert solve_sqrt_x_binary_search("") == ""
    assert solve_sqrt_x_binary_search(0) is True
    assert solve_sqrt_x_binary_search(-5) is False
