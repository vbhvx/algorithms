"""
Empirical benchmark for Boruvka Minimum Spanning Tree Contraction
"""
import time
from algorithms.practice.minimum_spanning_trees.boruvka_mst_algo import solve_boruvka_mst_algo

def benchmark_boruvka_mst_algo():
    start = time.perf_counter()
    for _ in range(100):
        solve_boruvka_mst_algo([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_boruvka_mst_algo()
    print(f"Boruvka Minimum Spanning Tree Contraction 100 iterations took {t*1000:.3f}ms")
