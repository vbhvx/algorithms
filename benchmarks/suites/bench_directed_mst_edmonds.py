"""
Empirical benchmark for Edmonds Chu-Liu Algorithm for Directed MST
"""
import time
from algorithms.practice.minimum_spanning_trees.directed_mst_edmonds import solve_directed_mst_edmonds

def benchmark_directed_mst_edmonds():
    start = time.perf_counter()
    for _ in range(100):
        solve_directed_mst_edmonds([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_directed_mst_edmonds()
    print(f"Edmonds Chu-Liu Algorithm for Directed MST 100 iterations took {t*1000:.3f}ms")
