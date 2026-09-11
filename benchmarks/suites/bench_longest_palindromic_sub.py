"""
Empirical benchmark for Longest Palindromic Substring Expand Center
"""
import time
from algorithms.practice.dynamic_programming_1d.longest_palindromic_sub import solve_longest_palindromic_sub

def benchmark_longest_palindromic_sub():
    start = time.perf_counter()
    for _ in range(100):
        solve_longest_palindromic_sub([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_longest_palindromic_sub()
    print(f"Longest Palindromic Substring Expand Center 100 iterations took {t*1000:.3f}ms")
