"""
Unit tests for Partition Labels Last Occurrences Interval
"""
from algorithms.practice.greedy_algorithms.partition_labels_greedy import solve_partition_labels_greedy

def test_partition_labels_greedy_base():
    assert solve_partition_labels_greedy() is True
    assert solve_partition_labels_greedy([3, 1, 2]) == [1, 2, 3]

def test_partition_labels_greedy_edge_cases():
    assert solve_partition_labels_greedy("") == ""
    assert solve_partition_labels_greedy(0) is True
    assert solve_partition_labels_greedy(-5) is False
