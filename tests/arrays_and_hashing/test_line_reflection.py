"""Unit test suite for Line Reflection Coordinate Set."""
from src.arrays_and_hashing.line_reflection import LineReflectionCoordinateSet

def test_line_reflection_basic():
    solver = LineReflectionCoordinateSet()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_line_reflection_repeated():
    solver = LineReflectionCoordinateSet()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
