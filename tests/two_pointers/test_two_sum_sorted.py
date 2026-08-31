"""Unit test suite for Two Sum II Sorted Pointers."""
from src.two_pointers.two_sum_sorted import TwoSumIiSortedPointers

def test_two_sum_sorted_basic():
    solver = TwoSumIiSortedPointers()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_two_sum_sorted_repeated():
    solver = TwoSumIiSortedPointers()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
