"""
Unit tests for Pairs of Songs Divisible by 60
"""
from algorithms.practice.arrays_and_hashing.songs_divisible_60 import solve_songs_divisible_60

def test_songs_divisible_60_base():
    assert solve_songs_divisible_60() is True
    assert solve_songs_divisible_60([3, 1, 2]) == [1, 2, 3]

def test_songs_divisible_60_edge_cases():
    assert solve_songs_divisible_60("") == ""
    assert solve_songs_divisible_60(0) is True
    assert solve_songs_divisible_60(-5) is False
