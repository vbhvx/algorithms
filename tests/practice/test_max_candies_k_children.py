"""
Unit tests for Maximum Candies Allocated to K Children
"""
from algorithms.practice.binary_search.max_candies_k_children import solve_max_candies_k_children

def test_max_candies_k_children_base():
    assert solve_max_candies_k_children() is True
    assert solve_max_candies_k_children([3, 1, 2]) == [1, 2, 3]

def test_max_candies_k_children_edge_cases():
    assert solve_max_candies_k_children("") == ""
    assert solve_max_candies_k_children(0) is True
    assert solve_max_candies_k_children(-5) is False
