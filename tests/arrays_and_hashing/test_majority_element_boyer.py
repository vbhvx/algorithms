"""Unit test suite for Majority Element Boyer Moore."""
from src.arrays_and_hashing.majority_element_boyer import MajorityElementBoyerMoore

def test_majority_element_boyer_basic():
    solver = MajorityElementBoyerMoore()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_majority_element_boyer_repeated():
    solver = MajorityElementBoyerMoore()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
