"""
Empirical benchmark for Interval List Intersections Two Pointers
"""
import time
from algorithms.practice.intervals_scheduling.interval_intersections import solve_interval_intersections

def benchmark_interval_intersections():
    start = time.perf_counter()
    for _ in range(100):
        solve_interval_intersections([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_interval_intersections()
    print(f"Interval List Intersections Two Pointers 100 iterations took {t*1000:.3f}ms")
