"""Unit test suite for Custom Sort String Frequency."""
from src.arrays_and_hashing.custom_sort_string import CustomSortStringFrequency

def test_custom_sort_string_basic():
    solver = CustomSortStringFrequency()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_custom_sort_string_repeated():
    solver = CustomSortStringFrequency()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
