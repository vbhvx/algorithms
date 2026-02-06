"""
Unit tests for Reverse String In Place
"""
from algorithms.practice.two_pointers.reverse_string import solve_reverse_string

def test_reverse_string_base():
    assert solve_reverse_string() is True
    assert solve_reverse_string([3, 1, 2]) == [1, 2, 3]

def test_reverse_string_edge_cases():
    assert solve_reverse_string("") == ""
    assert solve_reverse_string(0) is True
    assert solve_reverse_string(-5) is False
