"""Unit test suite for Insert Delete GetRandom O1."""
from src.arrays_and_hashing.randomized_set import InsertDeleteGetrandomO1

def test_randomized_set_basic():
    solver = InsertDeleteGetrandomO1()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_randomized_set_repeated():
    solver = InsertDeleteGetrandomO1()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
