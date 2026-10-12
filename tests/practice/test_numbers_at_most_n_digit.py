"""
Unit tests for Numbers At Most N Given Digit Set Digit DP
"""
from algorithms.practice.dynamic_programming_trees_bitmask.numbers_at_most_n_digit import solve_numbers_at_most_n_digit

def test_numbers_at_most_n_digit_base():
    assert solve_numbers_at_most_n_digit() is True
    assert solve_numbers_at_most_n_digit([3, 1, 2]) == [1, 2, 3]

def test_numbers_at_most_n_digit_edge_cases():
    assert solve_numbers_at_most_n_digit("") == ""
    assert solve_numbers_at_most_n_digit(0) is True
    assert solve_numbers_at_most_n_digit(-5) is False
