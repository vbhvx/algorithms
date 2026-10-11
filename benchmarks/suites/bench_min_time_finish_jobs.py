"""
Empirical benchmark for Minimum Time to Finish All Jobs Bitmask DP
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.min_time_finish_jobs import solve_min_time_finish_jobs

def benchmark_min_time_finish_jobs():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_time_finish_jobs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_time_finish_jobs()
    print(f"Minimum Time to Finish All Jobs Bitmask DP 100 iterations took {t*1000:.3f}ms")
