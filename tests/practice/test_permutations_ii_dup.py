"""
Unit tests for Permutations II Duplicate Elements Skip
"""
from algorithms.practice.backtracking.permutations_ii_dup import solve_permutations_ii_dup

def test_permutations_ii_dup_base():
    assert solve_permutations_ii_dup() is True
    assert solve_permutations_ii_dup([3, 1, 2]) == [1, 2, 3]

def test_permutations_ii_dup_edge_cases():
    assert solve_permutations_ii_dup("") == ""
    assert solve_permutations_ii_dup(0) is True
    assert solve_permutations_ii_dup(-5) is False
