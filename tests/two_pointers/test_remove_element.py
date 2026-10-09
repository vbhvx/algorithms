"""Unit test suite for Remove Element In Place Filter."""
from src.two_pointers.remove_element import RemoveElementInPlaceFilter

def test_remove_element_basic():
    solver = RemoveElementInPlaceFilter()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_remove_element_repeated():
    solver = RemoveElementInPlaceFilter()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
