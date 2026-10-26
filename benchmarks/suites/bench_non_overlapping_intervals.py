"""
Empirical benchmark for Non-overlapping Intervals Earliest End Time
"""
import time
from algorithms.practice.greedy_algorithms.non_overlapping_intervals import solve_non_overlapping_intervals

def benchmark_non_overlapping_intervals():
    start = time.perf_counter()
    for _ in range(100):
        solve_non_overlapping_intervals([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_non_overlapping_intervals()
    print(f"Non-overlapping Intervals Earliest End Time 100 iterations took {t*1000:.3f}ms")
