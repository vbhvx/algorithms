"""Unit test suite for Design HashSet Chaining Array."""
from src.arrays_and_hashing.design_hashset import DesignHashsetChainingArray

def test_design_hashset_basic():
    solver = DesignHashsetChainingArray()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_design_hashset_repeated():
    solver = DesignHashsetChainingArray()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
