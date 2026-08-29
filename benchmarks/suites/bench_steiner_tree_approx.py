"""
Empirical benchmark for Steiner Tree Minimum Weight Terminal Subgraph
"""
import time
from algorithms.practice.minimum_spanning_trees.steiner_tree_approx import solve_steiner_tree_approx

def benchmark_steiner_tree_approx():
    start = time.perf_counter()
    for _ in range(100):
        solve_steiner_tree_approx([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_steiner_tree_approx()
    print(f"Steiner Tree Minimum Weight Terminal Subgraph 100 iterations took {t*1000:.3f}ms")
