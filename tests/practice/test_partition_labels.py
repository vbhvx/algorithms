"""
Unit tests for Partition Labels Last Seen Index
"""
from algorithms.practice.two_pointers.partition_labels import solve_partition_labels

def test_partition_labels_base():
    assert solve_partition_labels() is True
    assert solve_partition_labels([3, 1, 2]) == [1, 2, 3]

def test_partition_labels_edge_cases():
    assert solve_partition_labels("") == ""
    assert solve_partition_labels(0) is True
    assert solve_partition_labels(-5) is False
