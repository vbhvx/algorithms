"""
Unit tests for Circular Array Loop Slow Fast
"""
from algorithms.practice.two_pointers.circular_array_loop import solve_circular_array_loop

def test_circular_array_loop_base():
    assert solve_circular_array_loop() is True
    assert solve_circular_array_loop([3, 1, 2]) == [1, 2, 3]

def test_circular_array_loop_edge_cases():
    assert solve_circular_array_loop("") == ""
    assert solve_circular_array_loop(0) is True
    assert solve_circular_array_loop(-5) is False
