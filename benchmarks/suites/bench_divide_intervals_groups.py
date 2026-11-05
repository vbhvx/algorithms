"""
Empirical benchmark for Divide Intervals Into Minimum Number of Groups
"""
import time
from algorithms.practice.intervals_scheduling.divide_intervals_groups import solve_divide_intervals_groups

def benchmark_divide_intervals_groups():
    start = time.perf_counter()
    for _ in range(100):
        solve_divide_intervals_groups([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_divide_intervals_groups()
    print(f"Divide Intervals Into Minimum Number of Groups 100 iterations took {t*1000:.3f}ms")
