"""
Unit tests for Remove Nth Node From End Fast Slow
"""
from algorithms.practice.linked_lists.remove_nth_node_end import solve_remove_nth_node_end

def test_remove_nth_node_end_base():
    assert solve_remove_nth_node_end() is True
    assert solve_remove_nth_node_end([3, 1, 2]) == [1, 2, 3]

def test_remove_nth_node_end_edge_cases():
    assert solve_remove_nth_node_end("") == ""
    assert solve_remove_nth_node_end(0) is True
    assert solve_remove_nth_node_end(-5) is False
