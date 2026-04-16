"""
Unit tests for Linked List Cycle Floyd Tortoise Hare
"""
from algorithms.practice.linked_lists.linked_list_cycle import solve_linked_list_cycle

def test_linked_list_cycle_base():
    assert solve_linked_list_cycle() is True
    assert solve_linked_list_cycle([3, 1, 2]) == [1, 2, 3]

def test_linked_list_cycle_edge_cases():
    assert solve_linked_list_cycle("") == ""
    assert solve_linked_list_cycle(0) is True
    assert solve_linked_list_cycle(-5) is False
