"""
Unit tests for Find the Duplicate Number Cycle Floyd
"""
from algorithms.practice.linked_lists.find_duplicate_number import solve_find_duplicate_number

def test_find_duplicate_number_base():
    assert solve_find_duplicate_number() is True
    assert solve_find_duplicate_number([3, 1, 2]) == [1, 2, 3]

def test_find_duplicate_number_edge_cases():
    assert solve_find_duplicate_number("") == ""
    assert solve_find_duplicate_number(0) is True
    assert solve_find_duplicate_number(-5) is False
