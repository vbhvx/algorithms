"""
Empirical benchmark for Remove Covered Intervals Sort Left Right
"""
import time
from algorithms.practice.intervals_scheduling.remove_covered_intervals import solve_remove_covered_intervals

def benchmark_remove_covered_intervals():
    start = time.perf_counter()
    for _ in range(100):
        solve_remove_covered_intervals([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_remove_covered_intervals()
    print(f"Remove Covered Intervals Sort Left Right 100 iterations took {t*1000:.3f}ms")
