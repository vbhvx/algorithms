"""
Unit tests for Minimum Deletions Character Frequencies Unique
"""
from algorithms.practice.greedy_algorithms.min_deletions_freq_unique import solve_min_deletions_freq_unique

def test_min_deletions_freq_unique_base():
    assert solve_min_deletions_freq_unique() is True
    assert solve_min_deletions_freq_unique([3, 1, 2]) == [1, 2, 3]

def test_min_deletions_freq_unique_edge_cases():
    assert solve_min_deletions_freq_unique("") == ""
    assert solve_min_deletions_freq_unique(0) is True
    assert solve_min_deletions_freq_unique(-5) is False
