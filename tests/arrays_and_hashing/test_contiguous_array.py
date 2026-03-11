"""Unit test suite for Contiguous Array Equal 0 1."""
from src.arrays_and_hashing.contiguous_array import ContiguousArrayEqual01

def test_contiguous_array_basic():
    solver = ContiguousArrayEqual01()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_contiguous_array_repeated():
    solver = ContiguousArrayEqual01()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
