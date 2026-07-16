"""
Unit tests for Palindrome Partitioning DFS Memo
"""
from algorithms.practice.backtracking.palindrome_partition import solve_palindrome_partition

def test_palindrome_partition_base():
    assert solve_palindrome_partition() is True
    assert solve_palindrome_partition([3, 1, 2]) == [1, 2, 3]

def test_palindrome_partition_edge_cases():
    assert solve_palindrome_partition("") == ""
    assert solve_palindrome_partition(0) is True
    assert solve_palindrome_partition(-5) is False
