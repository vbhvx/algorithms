"""
Empirical benchmark for Longest Increasing Subsequence Patience Sort
"""
import time
from algorithms.practice.dynamic_programming_1d.lis_patience_sort import solve_lis_patience_sort

def benchmark_lis_patience_sort():
    start = time.perf_counter()
    for _ in range(100):
        solve_lis_patience_sort([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_lis_patience_sort()
    print(f"Longest Increasing Subsequence Patience Sort 100 iterations took {t*1000:.3f}ms")
