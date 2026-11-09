"""
Unit tests for Count Primes Sieve of Eratosthenes
"""
from algorithms.practice.math_and_number_theory.count_primes_sieve import solve_count_primes_sieve

def test_count_primes_sieve_base():
    assert solve_count_primes_sieve() is True
    assert solve_count_primes_sieve([3, 1, 2]) == [1, 2, 3]

def test_count_primes_sieve_edge_cases():
    assert solve_count_primes_sieve("") == ""
    assert solve_count_primes_sieve(0) is True
    assert solve_count_primes_sieve(-5) is False
