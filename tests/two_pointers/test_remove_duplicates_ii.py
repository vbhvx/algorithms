"""Unit test suite for Remove Duplicates Sorted Array II."""
from src.two_pointers.remove_duplicates_ii import RemoveDuplicatesSortedArrayIi

def test_remove_duplicates_ii_basic():
    solver = RemoveDuplicatesSortedArrayIi()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_remove_duplicates_ii_repeated():
    solver = RemoveDuplicatesSortedArrayIi()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
