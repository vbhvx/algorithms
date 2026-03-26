"""
Empirical benchmark for Median of Two Sorted Arrays Partition
"""
import time
from algorithms.practice.binary_search.median_two_sorted import solve_median_two_sorted

def benchmark_median_two_sorted():
    start = time.perf_counter()
    for _ in range(100):
        solve_median_two_sorted([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_median_two_sorted()
    print(f"Median of Two Sorted Arrays Partition 100 iterations took {t*1000:.3f}ms")
