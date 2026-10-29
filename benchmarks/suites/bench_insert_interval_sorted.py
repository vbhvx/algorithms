"""
Empirical benchmark for Insert Interval Overlap Merging
"""
import time
from algorithms.practice.intervals_scheduling.insert_interval_sorted import solve_insert_interval_sorted

def benchmark_insert_interval_sorted():
    start = time.perf_counter()
    for _ in range(100):
        solve_insert_interval_sorted([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_insert_interval_sorted()
    print(f"Insert Interval Overlap Merging 100 iterations took {t*1000:.3f}ms")
