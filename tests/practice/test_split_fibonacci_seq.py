"""
Unit tests for Split Array into Fibonacci Sequence
"""
from algorithms.practice.backtracking.split_fibonacci_seq import solve_split_fibonacci_seq

def test_split_fibonacci_seq_base():
    assert solve_split_fibonacci_seq() is True
    assert solve_split_fibonacci_seq([3, 1, 2]) == [1, 2, 3]

def test_split_fibonacci_seq_edge_cases():
    assert solve_split_fibonacci_seq("") == ""
    assert solve_split_fibonacci_seq(0) is True
    assert solve_split_fibonacci_seq(-5) is False
