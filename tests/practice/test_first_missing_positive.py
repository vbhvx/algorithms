"""
Unit tests for First Missing Positive In Place
"""
from algorithms.practice.arrays_and_hashing.first_missing_positive import solve_first_missing_positive

def test_first_missing_positive_base():
    assert solve_first_missing_positive() is True
    assert solve_first_missing_positive([3, 1, 2]) == [1, 2, 3]

def test_first_missing_positive_edge_cases():
    assert solve_first_missing_positive("") == ""
    assert solve_first_missing_positive(0) is True
    assert solve_first_missing_positive(-5) is False
