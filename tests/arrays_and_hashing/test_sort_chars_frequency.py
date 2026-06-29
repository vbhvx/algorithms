"""Unit test suite for Sort Characters by Frequency."""
from src.arrays_and_hashing.sort_chars_frequency import SortCharactersByFrequency

def test_sort_chars_frequency_basic():
    solver = SortCharactersByFrequency()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_sort_chars_frequency_repeated():
    solver = SortCharactersByFrequency()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
