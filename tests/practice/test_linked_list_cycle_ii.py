"""
Unit tests for Linked List Cycle II Cycle Entry Point
"""
from algorithms.practice.linked_lists.linked_list_cycle_ii import solve_linked_list_cycle_ii

def test_linked_list_cycle_ii_base():
    assert solve_linked_list_cycle_ii() is True
    assert solve_linked_list_cycle_ii([3, 1, 2]) == [1, 2, 3]

def test_linked_list_cycle_ii_edge_cases():
    assert solve_linked_list_cycle_ii("") == ""
    assert solve_linked_list_cycle_ii(0) is True
    assert solve_linked_list_cycle_ii(-5) is False
