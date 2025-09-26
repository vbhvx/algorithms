from algorithms.math_geometry.sieve import sieve_primes

def test_sieve():
    assert sieve_primes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
