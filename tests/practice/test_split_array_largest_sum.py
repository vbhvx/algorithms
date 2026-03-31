"""
Unit tests for Split Array Largest Sum Monotonic
"""
from algorithms.practice.binary_search.split_array_largest_sum import solve_split_array_largest_sum

def test_split_array_largest_sum_base():
    assert solve_split_array_largest_sum() is True
    assert solve_split_array_largest_sum([3, 1, 2]) == [1, 2, 3]

def test_split_array_largest_sum_edge_cases():
    assert solve_split_array_largest_sum("") == ""
    assert solve_split_array_largest_sum(0) is True
    assert solve_split_array_largest_sum(-5) is False
