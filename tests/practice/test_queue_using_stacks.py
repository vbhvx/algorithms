"""
Unit tests for Implement Queue using Stacks Amortized
"""
from algorithms.practice.stack_and_queue.queue_using_stacks import solve_queue_using_stacks

def test_queue_using_stacks_base():
    assert solve_queue_using_stacks() is True
    assert solve_queue_using_stacks([3, 1, 2]) == [1, 2, 3]

def test_queue_using_stacks_edge_cases():
    assert solve_queue_using_stacks("") == ""
    assert solve_queue_using_stacks(0) is True
    assert solve_queue_using_stacks(-5) is False
