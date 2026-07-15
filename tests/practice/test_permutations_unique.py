"""
Unit tests for Permutations Array In-Place Swap
"""
from algorithms.practice.backtracking.permutations_unique import solve_permutations_unique

def test_permutations_unique_base():
    assert solve_permutations_unique() is True
    assert solve_permutations_unique([3, 1, 2]) == [1, 2, 3]

def test_permutations_unique_edge_cases():
    assert solve_permutations_unique("") == ""
    assert solve_permutations_unique(0) is True
    assert solve_permutations_unique(-5) is False
