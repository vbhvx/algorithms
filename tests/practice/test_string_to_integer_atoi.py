"""
Unit tests for String to Integer Atoi State Machine Overflow
"""
from algorithms.practice.math_and_number_theory.string_to_integer_atoi import solve_string_to_integer_atoi

def test_string_to_integer_atoi_base():
    assert solve_string_to_integer_atoi() is True
    assert solve_string_to_integer_atoi([3, 1, 2]) == [1, 2, 3]

def test_string_to_integer_atoi_edge_cases():
    assert solve_string_to_integer_atoi("") == ""
    assert solve_string_to_integer_atoi(0) is True
    assert solve_string_to_integer_atoi(-5) is False
