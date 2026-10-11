"""
Unit tests for Partition to K Equal Subsets Bitmask Memo
"""
from algorithms.practice.dynamic_programming_trees_bitmask.partition_k_subsets_bm import solve_partition_k_subsets_bm

def test_partition_k_subsets_bm_base():
    assert solve_partition_k_subsets_bm() is True
    assert solve_partition_k_subsets_bm([3, 1, 2]) == [1, 2, 3]

def test_partition_k_subsets_bm_edge_cases():
    assert solve_partition_k_subsets_bm("") == ""
    assert solve_partition_k_subsets_bm(0) is True
    assert solve_partition_k_subsets_bm(-5) is False
