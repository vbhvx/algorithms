"""
Empirical benchmark for Binary Tree Paths String Construction
"""
import time
from algorithms.practice.trees_and_bst.binary_tree_paths import solve_binary_tree_paths

def benchmark_binary_tree_paths():
    start = time.perf_counter()
    for _ in range(100):
        solve_binary_tree_paths([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_binary_tree_paths()
    print(f"Binary Tree Paths String Construction 100 iterations took {t*1000:.3f}ms")
