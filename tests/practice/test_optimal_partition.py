"""
Unit tests for Optimal Partition of String
"""
from algorithms.practice.arrays_and_hashing.optimal_partition import solve_optimal_partition

def test_optimal_partition_base():
    assert solve_optimal_partition() is True
    assert solve_optimal_partition([3, 1, 2]) == [1, 2, 3]

def test_optimal_partition_edge_cases():
    assert solve_optimal_partition("") == ""
    assert solve_optimal_partition(0) is True
    assert solve_optimal_partition(-5) is False
