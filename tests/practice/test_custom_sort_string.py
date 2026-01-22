"""
Unit tests for Custom Sort String Frequency
"""
from algorithms.practice.arrays_and_hashing.custom_sort_string import solve_custom_sort_string

def test_custom_sort_string_base():
    assert solve_custom_sort_string() is True
    assert solve_custom_sort_string([3, 1, 2]) == [1, 2, 3]

def test_custom_sort_string_edge_cases():
    assert solve_custom_sort_string("") == ""
    assert solve_custom_sort_string(0) is True
    assert solve_custom_sort_string(-5) is False
