"""
Unit tests for Reverse Integer Math Pop Push Overflow Check
"""
from algorithms.practice.math_and_number_theory.reverse_integer_overflow import solve_reverse_integer_overflow

def test_reverse_integer_overflow_base():
    assert solve_reverse_integer_overflow() is True
    assert solve_reverse_integer_overflow([3, 1, 2]) == [1, 2, 3]

def test_reverse_integer_overflow_edge_cases():
    assert solve_reverse_integer_overflow("") == ""
    assert solve_reverse_integer_overflow(0) is True
    assert solve_reverse_integer_overflow(-5) is False
