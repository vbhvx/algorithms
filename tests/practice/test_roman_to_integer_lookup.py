"""
Unit tests for Roman to Integer Subtraction Rule Lookup
"""
from algorithms.practice.math_and_number_theory.roman_to_integer_lookup import solve_roman_to_integer_lookup

def test_roman_to_integer_lookup_base():
    assert solve_roman_to_integer_lookup() is True
    assert solve_roman_to_integer_lookup([3, 1, 2]) == [1, 2, 3]

def test_roman_to_integer_lookup_edge_cases():
    assert solve_roman_to_integer_lookup("") == ""
    assert solve_roman_to_integer_lookup(0) is True
    assert solve_roman_to_integer_lookup(-5) is False
