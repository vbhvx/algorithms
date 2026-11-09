"""
Empirical benchmark for Count Primes Sieve of Eratosthenes
"""
import time
from algorithms.practice.math_and_number_theory.count_primes_sieve import solve_count_primes_sieve

def benchmark_count_primes_sieve():
    start = time.perf_counter()
    for _ in range(100):
        solve_count_primes_sieve([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_count_primes_sieve()
    print(f"Count Primes Sieve of Eratosthenes 100 iterations took {t*1000:.3f}ms")
