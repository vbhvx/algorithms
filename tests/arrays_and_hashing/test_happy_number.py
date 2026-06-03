"""Unit test suite for Happy Number Cycle Detection."""
from src.arrays_and_hashing.happy_number import HappyNumberCycleDetection

def test_happy_number_basic():
    solver = HappyNumberCycleDetection()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_happy_number_repeated():
    solver = HappyNumberCycleDetection()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
