"""
Unit tests for Implement Stack using Queues
"""
from algorithms.practice.stack_and_queue.stack_using_queues import solve_stack_using_queues

def test_stack_using_queues_base():
    assert solve_stack_using_queues() is True
    assert solve_stack_using_queues([3, 1, 2]) == [1, 2, 3]

def test_stack_using_queues_edge_cases():
    assert solve_stack_using_queues("") == ""
    assert solve_stack_using_queues(0) is True
    assert solve_stack_using_queues(-5) is False
