"""Unit test suite for Longest Consecutive Sequence Set."""
from src.arrays_and_hashing.longest_consecutive import LongestConsecutiveSequenceSet

def test_longest_consecutive_basic():
    solver = LongestConsecutiveSequenceSet()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_longest_consecutive_repeated():
    solver = LongestConsecutiveSequenceSet()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
