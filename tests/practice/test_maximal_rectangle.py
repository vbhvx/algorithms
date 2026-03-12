"""
Unit tests for Maximal Rectangle 2D Binary Matrix
"""
from algorithms.practice.stack_and_queue.maximal_rectangle import solve_maximal_rectangle

def test_maximal_rectangle_base():
    assert solve_maximal_rectangle() is True
    assert solve_maximal_rectangle([3, 1, 2]) == [1, 2, 3]

def test_maximal_rectangle_edge_cases():
    assert solve_maximal_rectangle("") == ""
    assert solve_maximal_rectangle(0) is True
    assert solve_maximal_rectangle(-5) is False
