"""Unit test suite for Word Pattern Bijective Mapping."""
from src.arrays_and_hashing.word_pattern import WordPatternBijectiveMapping

def test_word_pattern_basic():
    solver = WordPatternBijectiveMapping()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_word_pattern_repeated():
    solver = WordPatternBijectiveMapping()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
