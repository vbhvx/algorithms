"""
Empirical benchmark for Minimum Path Sum Matrix In-Place
"""
import time
from algorithms.practice.dynamic_programming_2d.min_path_sum_grid import solve_min_path_sum_grid

def benchmark_min_path_sum_grid():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_path_sum_grid([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_path_sum_grid()
    print(f"Minimum Path Sum Matrix In-Place 100 iterations took {t*1000:.3f}ms")
