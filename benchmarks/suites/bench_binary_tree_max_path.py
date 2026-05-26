"""
Empirical benchmark for Binary Tree Maximum Path Sum Kadane Tree
"""
import time
from algorithms.practice.trees_and_bst.binary_tree_max_path import solve_binary_tree_max_path

def benchmark_binary_tree_max_path():
    start = time.perf_counter()
    for _ in range(100):
        solve_binary_tree_max_path([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_binary_tree_max_path()
    print(f"Binary Tree Maximum Path Sum Kadane Tree 100 iterations took {t*1000:.3f}ms")
