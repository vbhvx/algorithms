"""
Unit tests for 132 Pattern Monotonic Stack Peak
"""
from algorithms.practice.stack_and_queue.pattern_132 import solve_pattern_132

def test_pattern_132_base():
    assert solve_pattern_132() is True
    assert solve_pattern_132([3, 1, 2]) == [1, 2, 3]

def test_pattern_132_edge_cases():
    assert solve_pattern_132("") == ""
    assert solve_pattern_132(0) is True
    assert solve_pattern_132(-5) is False
