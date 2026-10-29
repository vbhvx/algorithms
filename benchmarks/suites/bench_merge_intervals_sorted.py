"""
Empirical benchmark for Merge Intervals Start Time Sort
"""
import time
from algorithms.practice.intervals_scheduling.merge_intervals_sorted import solve_merge_intervals_sorted

def benchmark_merge_intervals_sorted():
    start = time.perf_counter()
    for _ in range(100):
        solve_merge_intervals_sorted([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_merge_intervals_sorted()
    print(f"Merge Intervals Start Time Sort 100 iterations took {t*1000:.3f}ms")
