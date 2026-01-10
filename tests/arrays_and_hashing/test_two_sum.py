"""Unit test suite for Two Sum Hash Map."""
from src.arrays_and_hashing.two_sum import TwoSumHashMap

def test_two_sum_basic():
    solver = TwoSumHashMap()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_two_sum_repeated():
    solver = TwoSumHashMap()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
