"""
Unit tests for Line Reflection Coordinate Set
"""
from algorithms.practice.arrays_and_hashing.line_reflection import solve_line_reflection

def test_line_reflection_base():
    assert solve_line_reflection() is True
    assert solve_line_reflection([3, 1, 2]) == [1, 2, 3]

def test_line_reflection_edge_cases():
    assert solve_line_reflection("") == ""
    assert solve_line_reflection(0) is True
    assert solve_line_reflection(-5) is False
