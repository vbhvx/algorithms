"""
Unit tests for Reverse Linked List In Place Iterative
"""
from algorithms.practice.linked_lists.reverse_linked_list import solve_reverse_linked_list

def test_reverse_linked_list_base():
    assert solve_reverse_linked_list() is True
    assert solve_reverse_linked_list([3, 1, 2]) == [1, 2, 3]

def test_reverse_linked_list_edge_cases():
    assert solve_reverse_linked_list("") == ""
    assert solve_reverse_linked_list(0) is True
    assert solve_reverse_linked_list(-5) is False
