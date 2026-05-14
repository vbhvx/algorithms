"""
Empirical benchmark for Balanced Binary Tree Height Balance Check
"""
import time
from algorithms.practice.trees_and_bst.balanced_binary_tree import solve_balanced_binary_tree

def benchmark_balanced_binary_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_balanced_binary_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_balanced_binary_tree()
    print(f"Balanced Binary Tree Height Balance Check 100 iterations took {t*1000:.3f}ms")
