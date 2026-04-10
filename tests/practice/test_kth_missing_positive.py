"""
Unit tests for Kth Missing Positive Number Bisect
"""
from algorithms.practice.binary_search.kth_missing_positive import solve_kth_missing_positive

def test_kth_missing_positive_base():
    assert solve_kth_missing_positive() is True
    assert solve_kth_missing_positive([3, 1, 2]) == [1, 2, 3]

def test_kth_missing_positive_edge_cases():
    assert solve_kth_missing_positive("") == ""
    assert solve_kth_missing_positive(0) is True
    assert solve_kth_missing_positive(-5) is False
