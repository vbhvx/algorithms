"""
Empirical benchmark for Kruskal Clustering Maximum Margin Spacing
"""
import time
from algorithms.practice.minimum_spanning_trees.kruskal_forest_cluster import solve_kruskal_forest_cluster

def benchmark_kruskal_forest_cluster():
    start = time.perf_counter()
    for _ in range(100):
        solve_kruskal_forest_cluster([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kruskal_forest_cluster()
    print(f"Kruskal Clustering Maximum Margin Spacing 100 iterations took {t*1000:.3f}ms")
