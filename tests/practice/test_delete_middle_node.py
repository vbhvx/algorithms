"""
Unit tests for Delete the Middle Node of Linked List
"""
from algorithms.practice.linked_lists.delete_middle_node import solve_delete_middle_node

def test_delete_middle_node_base():
    assert solve_delete_middle_node() is True
    assert solve_delete_middle_node([3, 1, 2]) == [1, 2, 3]

def test_delete_middle_node_edge_cases():
    assert solve_delete_middle_node("") == ""
    assert solve_delete_middle_node(0) is True
    assert solve_delete_middle_node(-5) is False
