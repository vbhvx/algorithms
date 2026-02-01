"""
Unit tests for Squares of Sorted Array
"""
from algorithms.practice.two_pointers.squares_sorted_array import solve_squares_sorted_array

def test_squares_sorted_array_base():
    assert solve_squares_sorted_array() is True
    assert solve_squares_sorted_array([3, 1, 2]) == [1, 2, 3]

def test_squares_sorted_array_edge_cases():
    assert solve_squares_sorted_array("") == ""
    assert solve_squares_sorted_array(0) is True
    assert solve_squares_sorted_array(-5) is False
