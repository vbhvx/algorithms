"""
Unit tests for Partition to K Equal Sum Subsets Bitmask
"""
from algorithms.practice.backtracking.partition_k_subsets import solve_partition_k_subsets

def test_partition_k_subsets_base():
    assert solve_partition_k_subsets() is True
    assert solve_partition_k_subsets([3, 1, 2]) == [1, 2, 3]

def test_partition_k_subsets_edge_cases():
    assert solve_partition_k_subsets("") == ""
    assert solve_partition_k_subsets(0) is True
    assert solve_partition_k_subsets(-5) is False
