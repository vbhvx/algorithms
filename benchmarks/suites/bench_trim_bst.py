"""
Empirical benchmark for Trim a Binary Search Tree Range Prune
"""
import time
from algorithms.practice.trees_and_bst.trim_bst import solve_trim_bst

def benchmark_trim_bst():
    start = time.perf_counter()
    for _ in range(100):
        solve_trim_bst([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_trim_bst()
    print(f"Trim a Binary Search Tree Range Prune 100 iterations took {t*1000:.3f}ms")
