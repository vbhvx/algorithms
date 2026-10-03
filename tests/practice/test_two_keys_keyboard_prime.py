"""
Unit tests for 2 Keys Keyboard Prime Factorization DP
"""
from algorithms.practice.dynamic_programming_2d.two_keys_keyboard_prime import solve_two_keys_keyboard_prime

def test_two_keys_keyboard_prime_base():
    assert solve_two_keys_keyboard_prime() is True
    assert solve_two_keys_keyboard_prime([3, 1, 2]) == [1, 2, 3]

def test_two_keys_keyboard_prime_edge_cases():
    assert solve_two_keys_keyboard_prime("") == ""
    assert solve_two_keys_keyboard_prime(0) is True
    assert solve_two_keys_keyboard_prime(-5) is False
