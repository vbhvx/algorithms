"""
Unit tests for Max Stack Dual Stack Tracking
"""
from algorithms.practice.stack_and_queue.max_stack import solve_max_stack

def test_max_stack_base():
    assert solve_max_stack() is True
    assert solve_max_stack([3, 1, 2]) == [1, 2, 3]

def test_max_stack_edge_cases():
    assert solve_max_stack("") == ""
    assert solve_max_stack(0) is True
    assert solve_max_stack(-5) is False
