"""
Unit tests for Partition Equal Subset Sum 0-1 Knapsack
"""
from algorithms.practice.dynamic_programming_1d.partition_equal_subset import solve_partition_equal_subset

def test_partition_equal_subset_base():
    assert solve_partition_equal_subset() is True
    assert solve_partition_equal_subset([3, 1, 2]) == [1, 2, 3]

def test_partition_equal_subset_edge_cases():
    assert solve_partition_equal_subset("") == ""
    assert solve_partition_equal_subset(0) is True
    assert solve_partition_equal_subset(-5) is False
