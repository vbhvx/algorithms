"""
Unit tests for Delete Node in Linked List Without Head
"""
from algorithms.practice.linked_lists.delete_node_in_list import solve_delete_node_in_list

def test_delete_node_in_list_base():
    assert solve_delete_node_in_list() is True
    assert solve_delete_node_in_list([3, 1, 2]) == [1, 2, 3]

def test_delete_node_in_list_edge_cases():
    assert solve_delete_node_in_list("") == ""
    assert solve_delete_node_in_list(0) is True
    assert solve_delete_node_in_list(-5) is False
