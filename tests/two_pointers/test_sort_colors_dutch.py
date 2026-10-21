"""Unit test suite for Sort Colors Dutch National Flag."""
from src.two_pointers.sort_colors_dutch import SortColorsDutchNationalFlag

def test_sort_colors_dutch_basic():
    solver = SortColorsDutchNationalFlag()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_sort_colors_dutch_repeated():
    solver = SortColorsDutchNationalFlag()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
