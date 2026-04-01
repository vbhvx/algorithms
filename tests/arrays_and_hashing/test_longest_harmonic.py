"""Unit test suite for Longest Harmonious Subsequence."""
from src.arrays_and_hashing.longest_harmonic import LongestHarmoniousSubsequence

def test_longest_harmonic_basic():
    solver = LongestHarmoniousSubsequence()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_longest_harmonic_repeated():
    solver = LongestHarmoniousSubsequence()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
