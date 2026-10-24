"""
Unit tests for Candy Distribution Left Right Pass Peak
"""
from algorithms.practice.greedy_algorithms.candy_distribution import solve_candy_distribution

def test_candy_distribution_base():
    assert solve_candy_distribution() is True
    assert solve_candy_distribution([3, 1, 2]) == [1, 2, 3]

def test_candy_distribution_edge_cases():
    assert solve_candy_distribution("") == ""
    assert solve_candy_distribution(0) is True
    assert solve_candy_distribution(-5) is False
