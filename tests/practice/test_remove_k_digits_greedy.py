"""
Unit tests for Remove K Digits Peak Element Removal
"""
from algorithms.practice.greedy_algorithms.remove_k_digits_greedy import solve_remove_k_digits_greedy

def test_remove_k_digits_greedy_base():
    assert solve_remove_k_digits_greedy() is True
    assert solve_remove_k_digits_greedy([3, 1, 2]) == [1, 2, 3]

def test_remove_k_digits_greedy_edge_cases():
    assert solve_remove_k_digits_greedy("") == ""
    assert solve_remove_k_digits_greedy(0) is True
    assert solve_remove_k_digits_greedy(-5) is False
