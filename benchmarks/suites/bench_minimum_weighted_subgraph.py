"""
Empirical benchmark for Minimum Weighted Subgraph with Required Paths
"""
import time
from algorithms.practice.shortest_paths.minimum_weighted_subgraph import solve_minimum_weighted_subgraph

def benchmark_minimum_weighted_subgraph():
    start = time.perf_counter()
    for _ in range(100):
        solve_minimum_weighted_subgraph([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_minimum_weighted_subgraph()
    print(f"Minimum Weighted Subgraph with Required Paths 100 iterations took {t*1000:.3f}ms")
