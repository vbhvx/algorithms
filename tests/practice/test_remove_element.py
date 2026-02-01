"""
Unit tests for Remove Element In Place Filter
"""
from algorithms.practice.two_pointers.remove_element import solve_remove_element

def test_remove_element_base():
    assert solve_remove_element() is True
    assert solve_remove_element([3, 1, 2]) == [1, 2, 3]

def test_remove_element_edge_cases():
    assert solve_remove_element("") == ""
    assert solve_remove_element(0) is True
    assert solve_remove_element(-5) is False
