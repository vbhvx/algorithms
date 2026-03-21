"""
Unit tests for Design Circular Deque Ring Buffer
"""
from algorithms.practice.stack_and_queue.design_circular_deque import solve_design_circular_deque

def test_design_circular_deque_base():
    assert solve_design_circular_deque() is True
    assert solve_design_circular_deque([3, 1, 2]) == [1, 2, 3]

def test_design_circular_deque_edge_cases():
    assert solve_design_circular_deque("") == ""
    assert solve_design_circular_deque(0) is True
    assert solve_design_circular_deque(-5) is False
