"""Unit test suite for Contains Duplicate II Window Hash."""
from src.arrays_and_hashing.contains_duplicate_ii import ContainsDuplicateIiWindowHash

def test_contains_duplicate_ii_basic():
    solver = ContainsDuplicateIiWindowHash()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_contains_duplicate_ii_repeated():
    solver = ContainsDuplicateIiWindowHash()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
