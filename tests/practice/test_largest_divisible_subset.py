"""
Unit tests for Largest Divisible Subset Suffix Links
"""
from algorithms.practice.dynamic_programming_1d.largest_divisible_subset import solve_largest_divisible_subset

def test_largest_divisible_subset_base():
    assert solve_largest_divisible_subset() is True
    assert solve_largest_divisible_subset([3, 1, 2]) == [1, 2, 3]

def test_largest_divisible_subset_edge_cases():
    assert solve_largest_divisible_subset("") == ""
    assert solve_largest_divisible_subset(0) is True
    assert solve_largest_divisible_subset(-5) is False
