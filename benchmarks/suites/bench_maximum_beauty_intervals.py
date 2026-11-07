"""
Empirical benchmark for Maximum Beauty of an Array After Operations
"""
import time
from algorithms.practice.intervals_scheduling.maximum_beauty_intervals import solve_maximum_beauty_intervals

def benchmark_maximum_beauty_intervals():
    start = time.perf_counter()
    for _ in range(100):
        solve_maximum_beauty_intervals([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_maximum_beauty_intervals()
    print(f"Maximum Beauty of an Array After Operations 100 iterations took {t*1000:.3f}ms")
