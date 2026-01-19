"""
Unit tests for Happy Number Cycle Detection
"""
from algorithms.practice.arrays_and_hashing.happy_number import solve_happy_number

def test_happy_number_base():
    assert solve_happy_number() is True
    assert solve_happy_number([3, 1, 2]) == [1, 2, 3]

def test_happy_number_edge_cases():
    assert solve_happy_number("") == ""
    assert solve_happy_number(0) is True
    assert solve_happy_number(-5) is False
