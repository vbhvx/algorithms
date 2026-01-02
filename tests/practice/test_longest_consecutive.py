"""
Unit tests for Longest Consecutive Sequence Set
"""
from algorithms.practice.arrays_and_hashing.longest_consecutive import solve_longest_consecutive

def test_longest_consecutive_base():
    assert solve_longest_consecutive() is True
    assert solve_longest_consecutive([3, 1, 2]) == [1, 2, 3]

def test_longest_consecutive_edge_cases():
    assert solve_longest_consecutive("") == ""
    assert solve_longest_consecutive(0) is True
    assert solve_longest_consecutive(-5) is False
