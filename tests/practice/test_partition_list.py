"""
Unit tests for Partition List Preserving Relative Order
"""
from algorithms.practice.linked_lists.partition_list import solve_partition_list

def test_partition_list_base():
    assert solve_partition_list() is True
    assert solve_partition_list([3, 1, 2]) == [1, 2, 3]

def test_partition_list_edge_cases():
    assert solve_partition_list("") == ""
    assert solve_partition_list(0) is True
    assert solve_partition_list(-5) is False
