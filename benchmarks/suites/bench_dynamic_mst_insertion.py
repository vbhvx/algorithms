"""
Empirical benchmark for Dynamic MST Edge Insertion and Cycle Removal
"""
import time
from algorithms.practice.minimum_spanning_trees.dynamic_mst_insertion import solve_dynamic_mst_insertion

def benchmark_dynamic_mst_insertion():
    start = time.perf_counter()
    for _ in range(100):
        solve_dynamic_mst_insertion([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_dynamic_mst_insertion()
    print(f"Dynamic MST Edge Insertion and Cycle Removal 100 iterations took {t*1000:.3f}ms")
