"""Unit test suite for Pairs of Songs Divisible by 60."""
from src.arrays_and_hashing.songs_divisible_60 import PairsOfSongsDivisibleBy60

def test_songs_divisible_60_basic():
    solver = PairsOfSongsDivisibleBy60()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_songs_divisible_60_repeated():
    solver = PairsOfSongsDivisibleBy60()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
