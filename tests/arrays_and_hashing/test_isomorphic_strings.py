"""Unit test suite for Isomorphic Strings Bijective."""
from src.arrays_and_hashing.isomorphic_strings import IsomorphicStringsBijective

def test_isomorphic_strings_basic():
    solver = IsomorphicStringsBijective()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_isomorphic_strings_repeated():
    solver = IsomorphicStringsBijective()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
