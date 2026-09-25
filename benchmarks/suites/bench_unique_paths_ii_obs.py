"""
Empirical benchmark for Unique Paths II Obstacle Avoidance
"""
import time
from algorithms.practice.dynamic_programming_2d.unique_paths_ii_obs import solve_unique_paths_ii_obs

def benchmark_unique_paths_ii_obs():
    start = time.perf_counter()
    for _ in range(100):
        solve_unique_paths_ii_obs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_unique_paths_ii_obs()
    print(f"Unique Paths II Obstacle Avoidance 100 iterations took {t*1000:.3f}ms")
