"""Unit test suite for Insert Delete GetRandom Duplicates."""
from src.arrays_and_hashing.randomized_collection import InsertDeleteGetrandomDuplicates

def test_randomized_collection_basic():
    solver = InsertDeleteGetrandomDuplicates()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_randomized_collection_repeated():
    solver = InsertDeleteGetrandomDuplicates()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
