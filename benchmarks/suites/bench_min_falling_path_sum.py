"""
Empirical benchmark for Minimum Falling Path Sum In-Place Row
"""
import time
from algorithms.practice.dynamic_programming_2d.min_falling_path_sum import solve_min_falling_path_sum

def benchmark_min_falling_path_sum():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_falling_path_sum([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_falling_path_sum()
    print(f"Minimum Falling Path Sum In-Place Row 100 iterations took {t*1000:.3f}ms")
