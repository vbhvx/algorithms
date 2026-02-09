"""
Unit tests for Array Partition Min Pair Sum
"""
from algorithms.practice.two_pointers.array_partition import solve_array_partition

def test_array_partition_base():
    assert solve_array_partition() is True
    assert solve_array_partition([3, 1, 2]) == [1, 2, 3]

def test_array_partition_edge_cases():
    assert solve_array_partition("") == ""
    assert solve_array_partition(0) is True
    assert solve_array_partition(-5) is False
