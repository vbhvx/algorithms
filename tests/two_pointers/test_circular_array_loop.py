"""Unit test suite for Circular Array Loop Slow Fast."""
from src.two_pointers.circular_array_loop import CircularArrayLoopSlowFast

def test_circular_array_loop_basic():
    solver = CircularArrayLoopSlowFast()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_circular_array_loop_repeated():
    solver = CircularArrayLoopSlowFast()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
