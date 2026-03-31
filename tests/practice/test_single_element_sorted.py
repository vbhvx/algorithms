"""
Unit tests for Single Element in Sorted Array Parity
"""
from algorithms.practice.binary_search.single_element_sorted import solve_single_element_sorted

def test_single_element_sorted_base():
    assert solve_single_element_sorted() is True
    assert solve_single_element_sorted([3, 1, 2]) == [1, 2, 3]

def test_single_element_sorted_edge_cases():
    assert solve_single_element_sorted("") == ""
    assert solve_single_element_sorted(0) is True
    assert solve_single_element_sorted(-5) is False
