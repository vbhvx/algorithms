"""Unit test suite for Backspace String Compare Reverse."""
from src.two_pointers.backspace_compare import BackspaceStringCompareReverse

def test_backspace_compare_basic():
    solver = BackspaceStringCompareReverse()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_backspace_compare_repeated():
    solver = BackspaceStringCompareReverse()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
