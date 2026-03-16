"""
Unit tests for Next Greater Element II Circular Stack
"""
from algorithms.practice.stack_and_queue.next_greater_element_ii import solve_next_greater_element_ii

def test_next_greater_element_ii_base():
    assert solve_next_greater_element_ii() is True
    assert solve_next_greater_element_ii([3, 1, 2]) == [1, 2, 3]

def test_next_greater_element_ii_edge_cases():
    assert solve_next_greater_element_ii("") == ""
    assert solve_next_greater_element_ii(0) is True
    assert solve_next_greater_element_ii(-5) is False
