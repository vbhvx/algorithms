"""Sieve of Eratosthenes generating all primes up to N."""
from typing import List

def sieve_primes(n: int) -> List[int]:
    if n < 2: return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p): is_prime[i] = False
    return [p for p in range(2, n + 1) if is_prime[p]]
