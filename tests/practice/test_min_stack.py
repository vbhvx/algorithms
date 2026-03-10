"""
Unit tests for Min Stack O1 Operations
"""
from algorithms.practice.stack_and_queue.min_stack import solve_min_stack

def test_min_stack_base():
    assert solve_min_stack() is True
    assert solve_min_stack([3, 1, 2]) == [1, 2, 3]

def test_min_stack_edge_cases():
    assert solve_min_stack("") == ""
    assert solve_min_stack(0) is True
    assert solve_min_stack(-5) is False
