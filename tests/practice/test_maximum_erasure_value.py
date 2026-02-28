"""
Unit tests for Maximum Erasure Value Unique Window
"""
from algorithms.practice.sliding_window.maximum_erasure_value import solve_maximum_erasure_value

def test_maximum_erasure_value_base():
    assert solve_maximum_erasure_value() is True
    assert solve_maximum_erasure_value([3, 1, 2]) == [1, 2, 3]

def test_maximum_erasure_value_edge_cases():
    assert solve_maximum_erasure_value("") == ""
    assert solve_maximum_erasure_value(0) is True
    assert solve_maximum_erasure_value(-5) is False
