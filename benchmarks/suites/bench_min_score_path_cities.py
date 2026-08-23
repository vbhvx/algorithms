"""
Empirical benchmark for Minimum Score of a Path Between Two Cities DSU
"""
import time
from algorithms.practice.minimum_spanning_trees.min_score_path_cities import solve_min_score_path_cities

def benchmark_min_score_path_cities():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_score_path_cities([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_score_path_cities()
    print(f"Minimum Score of a Path Between Two Cities DSU 100 iterations took {t*1000:.3f}ms")
