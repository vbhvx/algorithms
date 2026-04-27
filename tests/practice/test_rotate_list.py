"""
Unit tests for Rotate List Circular Break Point
"""
from algorithms.practice.linked_lists.rotate_list import solve_rotate_list

def test_rotate_list_base():
    assert solve_rotate_list() is True
    assert solve_rotate_list([3, 1, 2]) == [1, 2, 3]

def test_rotate_list_edge_cases():
    assert solve_rotate_list("") == ""
    assert solve_rotate_list(0) is True
    assert solve_rotate_list(-5) is False
