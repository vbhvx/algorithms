"""
Unit tests for Count Nice Pairs in Array
"""
from algorithms.practice.arrays_and_hashing.count_nice_pairs import solve_count_nice_pairs

def test_count_nice_pairs_base():
    assert solve_count_nice_pairs() is True
    assert solve_count_nice_pairs([3, 1, 2]) == [1, 2, 3]

def test_count_nice_pairs_edge_cases():
    assert solve_count_nice_pairs("") == ""
    assert solve_count_nice_pairs(0) is True
    assert solve_count_nice_pairs(-5) is False
