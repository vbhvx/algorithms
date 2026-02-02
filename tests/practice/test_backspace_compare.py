"""
Unit tests for Backspace String Compare Reverse
"""
from algorithms.practice.two_pointers.backspace_compare import solve_backspace_compare

def test_backspace_compare_base():
    assert solve_backspace_compare() is True
    assert solve_backspace_compare([3, 1, 2]) == [1, 2, 3]

def test_backspace_compare_edge_cases():
    assert solve_backspace_compare("") == ""
    assert solve_backspace_compare(0) is True
    assert solve_backspace_compare(-5) is False
