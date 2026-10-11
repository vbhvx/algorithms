"""Unit test suite for Squares of Sorted Array."""
from src.two_pointers.squares_sorted_array import SquaresOfSortedArray

def test_squares_sorted_array_basic():
    solver = SquaresOfSortedArray()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_squares_sorted_array_repeated():
    solver = SquaresOfSortedArray()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
