"""
Unit tests for Validate Stack Sequences Pop Simulation
"""
from algorithms.practice.stack_and_queue.validate_stack_seq import solve_validate_stack_seq

def test_validate_stack_seq_base():
    assert solve_validate_stack_seq() is True
    assert solve_validate_stack_seq([3, 1, 2]) == [1, 2, 3]

def test_validate_stack_seq_edge_cases():
    assert solve_validate_stack_seq("") == ""
    assert solve_validate_stack_seq(0) is True
    assert solve_validate_stack_seq(-5) is False
