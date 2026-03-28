"""
Unit tests for Find Peak Element Logarithmic Ascent
"""
from algorithms.practice.binary_search.find_peak_element import solve_find_peak_element

def test_find_peak_element_base():
    assert solve_find_peak_element() is True
    assert solve_find_peak_element([3, 1, 2]) == [1, 2, 3]

def test_find_peak_element_edge_cases():
    assert solve_find_peak_element("") == ""
    assert solve_find_peak_element(0) is True
    assert solve_find_peak_element(-5) is False
