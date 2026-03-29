"""Unit test suite for First Missing Positive In Place."""
from src.arrays_and_hashing.first_missing_positive import FirstMissingPositiveInPlace

def test_first_missing_positive_basic():
    solver = FirstMissingPositiveInPlace()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_first_missing_positive_repeated():
    solver = FirstMissingPositiveInPlace()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
