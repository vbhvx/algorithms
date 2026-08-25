"""
Empirical benchmark for Degree-Constrained MST Heuristic Approximation
"""
import time
from algorithms.practice.minimum_spanning_trees.degree_constrained_mst import solve_degree_constrained_mst

def benchmark_degree_constrained_mst():
    start = time.perf_counter()
    for _ in range(100):
        solve_degree_constrained_mst([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_degree_constrained_mst()
    print(f"Degree-Constrained MST Heuristic Approximation 100 iterations took {t*1000:.3f}ms")
