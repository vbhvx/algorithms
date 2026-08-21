"""
Empirical benchmark for Find Critical and Pseudo-Critical Edges in MST
"""
import time
from algorithms.practice.minimum_spanning_trees.critical_pseudo_edges import solve_critical_pseudo_edges

def benchmark_critical_pseudo_edges():
    start = time.perf_counter()
    for _ in range(100):
        solve_critical_pseudo_edges([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_critical_pseudo_edges()
    print(f"Find Critical and Pseudo-Critical Edges in MST 100 iterations took {t*1000:.3f}ms")
