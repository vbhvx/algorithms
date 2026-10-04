"""Unit test suite for Remove Duplicates Sorted Array."""
from src.two_pointers.remove_duplicates_sorted import RemoveDuplicatesSortedArray

def test_remove_duplicates_sorted_basic():
    solver = RemoveDuplicatesSortedArray()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_remove_duplicates_sorted_repeated():
    solver = RemoveDuplicatesSortedArray()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
