"""Unit test suite for Valid Anagram Counter."""
from src.arrays_and_hashing.valid_anagram import ValidAnagramCounter

def test_valid_anagram_basic():
    solver = ValidAnagramCounter()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_valid_anagram_repeated():
    solver = ValidAnagramCounter()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
