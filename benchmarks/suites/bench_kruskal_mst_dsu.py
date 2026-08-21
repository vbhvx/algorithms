"""
Empirical benchmark for Kruskal Minimum Spanning Tree DSU Rank
"""
import time
from algorithms.practice.minimum_spanning_trees.kruskal_mst_dsu import solve_kruskal_mst_dsu

def benchmark_kruskal_mst_dsu():
    start = time.perf_counter()
    for _ in range(100):
        solve_kruskal_mst_dsu([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kruskal_mst_dsu()
    print(f"Kruskal Minimum Spanning Tree DSU Rank 100 iterations took {t*1000:.3f}ms")
