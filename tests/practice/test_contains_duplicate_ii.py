"""
Unit tests for Contains Duplicate II Window Hash
"""
from algorithms.practice.arrays_and_hashing.contains_duplicate_ii import solve_contains_duplicate_ii

def test_contains_duplicate_ii_base():
    assert solve_contains_duplicate_ii() is True
    assert solve_contains_duplicate_ii([3, 1, 2]) == [1, 2, 3]

def test_contains_duplicate_ii_edge_cases():
    assert solve_contains_duplicate_ii("") == ""
    assert solve_contains_duplicate_ii(0) is True
    assert solve_contains_duplicate_ii(-5) is False
