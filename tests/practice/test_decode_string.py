"""
Unit tests for Decode String Nested Multipliers
"""
from algorithms.practice.stack_and_queue.decode_string import solve_decode_string

def test_decode_string_base():
    assert solve_decode_string() is True
    assert solve_decode_string([3, 1, 2]) == [1, 2, 3]

def test_decode_string_edge_cases():
    assert solve_decode_string("") == ""
    assert solve_decode_string(0) is True
    assert solve_decode_string(-5) is False
