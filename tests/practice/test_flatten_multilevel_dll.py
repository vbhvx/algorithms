"""
Unit tests for Flatten Multilevel Doubly Linked List
"""
from algorithms.practice.linked_lists.flatten_multilevel_dll import solve_flatten_multilevel_dll

def test_flatten_multilevel_dll_base():
    assert solve_flatten_multilevel_dll() is True
    assert solve_flatten_multilevel_dll([3, 1, 2]) == [1, 2, 3]

def test_flatten_multilevel_dll_edge_cases():
    assert solve_flatten_multilevel_dll("") == ""
    assert solve_flatten_multilevel_dll(0) is True
    assert solve_flatten_multilevel_dll(-5) is False
