"""
Unit tests for Add Two Numbers Digit Carry Traversal
"""
from algorithms.practice.linked_lists.add_two_numbers import solve_add_two_numbers

def test_add_two_numbers_base():
    assert solve_add_two_numbers() is True
    assert solve_add_two_numbers([3, 1, 2]) == [1, 2, 3]

def test_add_two_numbers_edge_cases():
    assert solve_add_two_numbers("") == ""
    assert solve_add_two_numbers(0) is True
    assert solve_add_two_numbers(-5) is False
