"""
Unit tests for Flatten Nested List Iterator Stack
"""
from algorithms.practice.stack_and_queue.flatten_nested_list import solve_flatten_nested_list

def test_flatten_nested_list_base():
    assert solve_flatten_nested_list() is True
    assert solve_flatten_nested_list([3, 1, 2]) == [1, 2, 3]

def test_flatten_nested_list_edge_cases():
    assert solve_flatten_nested_list("") == ""
    assert solve_flatten_nested_list(0) is True
    assert solve_flatten_nested_list(-5) is False
