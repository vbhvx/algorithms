"""Unit test suite for Find All Anagrams Sliding Window."""
from src.arrays_and_hashing.find_all_anagrams import FindAllAnagramsSlidingWindow

def test_find_all_anagrams_basic():
    solver = FindAllAnagramsSlidingWindow()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_find_all_anagrams_repeated():
    solver = FindAllAnagramsSlidingWindow()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
