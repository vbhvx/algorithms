"""
Empirical benchmark for Minimum Height Trees Leaf Trimming In-Degree
"""
import time
from algorithms.practice.graphs_and_traversals.min_height_trees import solve_min_height_trees

def benchmark_min_height_trees():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_height_trees([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_height_trees()
    print(f"Minimum Height Trees Leaf Trimming In-Degree 100 iterations took {t*1000:.3f}ms")
