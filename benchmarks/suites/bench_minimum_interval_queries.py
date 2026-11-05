"""
Empirical benchmark for Minimum Interval to Include Each Query Offline
"""
import time
from algorithms.practice.intervals_scheduling.minimum_interval_queries import solve_minimum_interval_queries

def benchmark_minimum_interval_queries():
    start = time.perf_counter()
    for _ in range(100):
        solve_minimum_interval_queries([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_minimum_interval_queries()
    print(f"Minimum Interval to Include Each Query Offline 100 iterations took {t*1000:.3f}ms")
