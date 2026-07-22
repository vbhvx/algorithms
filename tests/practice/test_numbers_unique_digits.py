"""
Unit tests for Count Numbers with Unique Digits Combinatorics
"""
from algorithms.practice.backtracking.numbers_unique_digits import solve_numbers_unique_digits

def test_numbers_unique_digits_base():
    assert solve_numbers_unique_digits() is True
    assert solve_numbers_unique_digits([3, 1, 2]) == [1, 2, 3]

def test_numbers_unique_digits_edge_cases():
    assert solve_numbers_unique_digits("") == ""
    assert solve_numbers_unique_digits(0) is True
    assert solve_numbers_unique_digits(-5) is False
