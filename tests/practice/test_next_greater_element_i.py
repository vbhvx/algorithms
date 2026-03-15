"""
Unit tests for Next Greater Element I Monotonic Hash
"""
from algorithms.practice.stack_and_queue.next_greater_element_i import solve_next_greater_element_i

def test_next_greater_element_i_base():
    assert solve_next_greater_element_i() is True
    assert solve_next_greater_element_i([3, 1, 2]) == [1, 2, 3]

def test_next_greater_element_i_edge_cases():
    assert solve_next_greater_element_i("") == ""
    assert solve_next_greater_element_i(0) is True
    assert solve_next_greater_element_i(-5) is False
