"""
Unit tests for Subsets II with Duplicates Skip Sorted
"""
from algorithms.practice.backtracking.subsets_ii_duplicates import solve_subsets_ii_duplicates

def test_subsets_ii_duplicates_base():
    assert solve_subsets_ii_duplicates() is True
    assert solve_subsets_ii_duplicates([3, 1, 2]) == [1, 2, 3]

def test_subsets_ii_duplicates_edge_cases():
    assert solve_subsets_ii_duplicates("") == ""
    assert solve_subsets_ii_duplicates(0) is True
    assert solve_subsets_ii_duplicates(-5) is False
