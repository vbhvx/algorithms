"""
Empirical benchmark for Minimum Interval to Include Each Query MinHeap
"""
import time
from algorithms.practice.heaps_and_priority.minimum_interval_query import solve_minimum_interval_query

def benchmark_minimum_interval_query():
    start = time.perf_counter()
    for _ in range(100):
        solve_minimum_interval_query([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_minimum_interval_query()
    print(f"Minimum Interval to Include Each Query MinHeap 100 iterations took {t*1000:.3f}ms")
