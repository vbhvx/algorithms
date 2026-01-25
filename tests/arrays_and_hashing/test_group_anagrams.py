"""Unit test suite for Group Anagrams Sorted Key."""
from src.arrays_and_hashing.group_anagrams import GroupAnagramsSortedKey

def test_group_anagrams_basic():
    solver = GroupAnagramsSortedKey()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_group_anagrams_repeated():
    solver = GroupAnagramsSortedKey()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
