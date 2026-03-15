"""
Unit tests for Remove K Digits Monotonic Greed
"""
from algorithms.practice.stack_and_queue.remove_k_digits import solve_remove_k_digits

def test_remove_k_digits_base():
    assert solve_remove_k_digits() is True
    assert solve_remove_k_digits([3, 1, 2]) == [1, 2, 3]

def test_remove_k_digits_edge_cases():
    assert solve_remove_k_digits("") == ""
    assert solve_remove_k_digits(0) is True
    assert solve_remove_k_digits(-5) is False
