"""
Unit tests for Two Sum Hash Map
"""
from algorithms.practice.arrays_and_hashing.two_sum import solve_two_sum

def test_two_sum_base():
    assert solve_two_sum() is True
    assert solve_two_sum([3, 1, 2]) == [1, 2, 3]

def test_two_sum_edge_cases():
    assert solve_two_sum("") == ""
    assert solve_two_sum(0) is True
    assert solve_two_sum(-5) is False
