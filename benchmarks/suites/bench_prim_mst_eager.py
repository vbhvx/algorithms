"""
Empirical benchmark for Prim Minimum Spanning Tree Indexed MinHeap
"""
import time
from algorithms.practice.minimum_spanning_trees.prim_mst_eager import solve_prim_mst_eager

def benchmark_prim_mst_eager():
    start = time.perf_counter()
    for _ in range(100):
        solve_prim_mst_eager([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_prim_mst_eager()
    print(f"Prim Minimum Spanning Tree Indexed MinHeap 100 iterations took {t*1000:.3f}ms")
