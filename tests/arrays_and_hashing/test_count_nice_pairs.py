"""Unit test suite for Count Nice Pairs in Array."""
from src.arrays_and_hashing.count_nice_pairs import CountNicePairsInArray

def test_count_nice_pairs_basic():
    solver = CountNicePairsInArray()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_count_nice_pairs_repeated():
    solver = CountNicePairsInArray()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
