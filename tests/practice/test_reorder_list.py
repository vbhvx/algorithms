"""
Unit tests for Reorder List Reverse Second Half Interleave
"""
from algorithms.practice.linked_lists.reorder_list import solve_reorder_list

def test_reorder_list_base():
    assert solve_reorder_list() is True
    assert solve_reorder_list([3, 1, 2]) == [1, 2, 3]

def test_reorder_list_edge_cases():
    assert solve_reorder_list("") == ""
    assert solve_reorder_list(0) is True
    assert solve_reorder_list(-5) is False
