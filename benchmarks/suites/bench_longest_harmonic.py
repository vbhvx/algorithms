"""
Empirical benchmark for Longest Harmonious Subsequence
"""
import time
from algorithms.practice.arrays_and_hashing.longest_harmonic import solve_longest_harmonic

def benchmark_longest_harmonic():
    start = time.perf_counter()
    for _ in range(100):
        solve_longest_harmonic([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_longest_harmonic()
    print(f"Longest Harmonious Subsequence 100 iterations took {t*1000:.3f}ms")
