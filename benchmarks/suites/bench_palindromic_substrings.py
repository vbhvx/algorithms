"""
Empirical benchmark for Palindromic Substrings Center Count
"""
import time
from algorithms.practice.dynamic_programming_1d.palindromic_substrings import solve_palindromic_substrings

def benchmark_palindromic_substrings():
    start = time.perf_counter()
    for _ in range(100):
        solve_palindromic_substrings([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_palindromic_substrings()
    print(f"Palindromic Substrings Center Count 100 iterations took {t*1000:.3f}ms")
