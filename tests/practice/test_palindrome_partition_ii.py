"""
Unit tests for Palindrome Partitioning II Minimum Cuts
"""
from algorithms.practice.dynamic_programming_2d.palindrome_partition_ii import solve_palindrome_partition_ii

def test_palindrome_partition_ii_base():
    assert solve_palindrome_partition_ii() is True
    assert solve_palindrome_partition_ii([3, 1, 2]) == [1, 2, 3]

def test_palindrome_partition_ii_edge_cases():
    assert solve_palindrome_partition_ii("") == ""
    assert solve_palindrome_partition_ii(0) is True
    assert solve_palindrome_partition_ii(-5) is False
