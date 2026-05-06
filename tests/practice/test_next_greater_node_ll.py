"""
Unit tests for Next Greater Node in Linked List Monotonic
"""
from algorithms.practice.linked_lists.next_greater_node_ll import solve_next_greater_node_ll

def test_next_greater_node_ll_base():
    assert solve_next_greater_node_ll() is True
    assert solve_next_greater_node_ll([3, 1, 2]) == [1, 2, 3]

def test_next_greater_node_ll_edge_cases():
    assert solve_next_greater_node_ll("") == ""
    assert solve_next_greater_node_ll(0) is True
    assert solve_next_greater_node_ll(-5) is False
