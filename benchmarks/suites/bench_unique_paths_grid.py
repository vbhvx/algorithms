"""
Empirical benchmark for Unique Paths Combinatorics Dynamic Programming
"""
import time
from algorithms.practice.dynamic_programming_2d.unique_paths_grid import solve_unique_paths_grid

def benchmark_unique_paths_grid():
    start = time.perf_counter()
    for _ in range(100):
        solve_unique_paths_grid([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_unique_paths_grid()
    print(f"Unique Paths Combinatorics Dynamic Programming 100 iterations took {t*1000:.3f}ms")
