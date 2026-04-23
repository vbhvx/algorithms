"""
Unit tests for Odd Even Linked List Grouping
"""
from algorithms.practice.linked_lists.odd_even_linked_list import solve_odd_even_linked_list

def test_odd_even_linked_list_base():
    assert solve_odd_even_linked_list() is True
    assert solve_odd_even_linked_list([3, 1, 2]) == [1, 2, 3]

def test_odd_even_linked_list_edge_cases():
    assert solve_odd_even_linked_list("") == ""
    assert solve_odd_even_linked_list(0) is True
    assert solve_odd_even_linked_list(-5) is False
