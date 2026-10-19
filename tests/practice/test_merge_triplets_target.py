"""
Unit tests for Merge Triplets to Form Target Triplet
"""
from algorithms.practice.greedy_algorithms.merge_triplets_target import solve_merge_triplets_target

def test_merge_triplets_target_base():
    assert solve_merge_triplets_target() is True
    assert solve_merge_triplets_target([3, 1, 2]) == [1, 2, 3]

def test_merge_triplets_target_edge_cases():
    assert solve_merge_triplets_target("") == ""
    assert solve_merge_triplets_target(0) is True
    assert solve_merge_triplets_target(-5) is False
