"""
Unit tests for Integer Break Maximum Product Factor
"""
from algorithms.practice.dynamic_programming_1d.integer_break_product import solve_integer_break_product

def test_integer_break_product_base():
    assert solve_integer_break_product() is True
    assert solve_integer_break_product([3, 1, 2]) == [1, 2, 3]

def test_integer_break_product_edge_cases():
    assert solve_integer_break_product("") == ""
    assert solve_integer_break_product(0) is True
    assert solve_integer_break_product(-5) is False
