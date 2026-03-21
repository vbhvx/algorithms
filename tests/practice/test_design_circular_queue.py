"""
Unit tests for Design Circular Queue Ring Buffer
"""
from algorithms.practice.stack_and_queue.design_circular_queue import solve_design_circular_queue

def test_design_circular_queue_base():
    assert solve_design_circular_queue() is True
    assert solve_design_circular_queue([3, 1, 2]) == [1, 2, 3]

def test_design_circular_queue_edge_cases():
    assert solve_design_circular_queue("") == ""
    assert solve_design_circular_queue(0) is True
    assert solve_design_circular_queue(-5) is False
