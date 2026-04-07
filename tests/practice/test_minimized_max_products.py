"""
Unit tests for Minimized Maximum of Products in Stores
"""
from algorithms.practice.binary_search.minimized_max_products import solve_minimized_max_products

def test_minimized_max_products_base():
    assert solve_minimized_max_products() is True
    assert solve_minimized_max_products([3, 1, 2]) == [1, 2, 3]

def test_minimized_max_products_edge_cases():
    assert solve_minimized_max_products("") == ""
    assert solve_minimized_max_products(0) is True
    assert solve_minimized_max_products(-5) is False
