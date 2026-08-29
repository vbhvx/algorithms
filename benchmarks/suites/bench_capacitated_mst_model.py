"""
Empirical benchmark for Capacitated Minimum Spanning Tree Tree DP
"""
import time
from algorithms.practice.minimum_spanning_trees.capacitated_mst_model import solve_capacitated_mst_model

def benchmark_capacitated_mst_model():
    start = time.perf_counter()
    for _ in range(100):
        solve_capacitated_mst_model([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_capacitated_mst_model()
    print(f"Capacitated Minimum Spanning Tree Tree DP 100 iterations took {t*1000:.3f}ms")
