"""
Empirical benchmark for Subtree of Another Tree Hash or DFS
"""
import time
from algorithms.practice.trees_and_bst.is_subtree import solve_is_subtree

def benchmark_is_subtree():
    start = time.perf_counter()
    for _ in range(100):
        solve_is_subtree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_is_subtree()
    print(f"Subtree of Another Tree Hash or DFS 100 iterations took {t*1000:.3f}ms")
