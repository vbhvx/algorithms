"""Unit test suite for Design HashMap Chaining Array."""
from src.arrays_and_hashing.design_hashmap import DesignHashmapChainingArray

def test_design_hashmap_basic():
    solver = DesignHashmapChainingArray()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_design_hashmap_repeated():
    solver = DesignHashmapChainingArray()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
