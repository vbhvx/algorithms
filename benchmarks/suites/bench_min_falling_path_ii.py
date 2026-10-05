"""
Empirical benchmark for Minimum Falling Path Sum II Running Two Mins
"""
import time
from algorithms.practice.dynamic_programming_2d.min_falling_path_ii import solve_min_falling_path_ii

def benchmark_min_falling_path_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_falling_path_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_falling_path_ii()
    print(f"Minimum Falling Path Sum II Running Two Mins 100 iterations took {t*1000:.3f}ms")
