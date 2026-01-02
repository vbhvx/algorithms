"""
Unit tests for Product of Array Except Self
"""
from algorithms.practice.arrays_and_hashing.product_except_self import solve_product_except_self

def test_product_except_self_base():
    assert solve_product_except_self() is True
    assert solve_product_except_self([3, 1, 2]) == [1, 2, 3]

def test_product_except_self_edge_cases():
    assert solve_product_except_self("") == ""
    assert solve_product_except_self(0) is True
    assert solve_product_except_self(-5) is False
