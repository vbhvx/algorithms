"""
Empirical benchmark for Maximum Sum BST in Binary Tree Subtree Range
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.max_sum_bst_binary import solve_max_sum_bst_binary

def benchmark_max_sum_bst_binary():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_sum_bst_binary([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_sum_bst_binary()
    print(f"Maximum Sum BST in Binary Tree Subtree Range 100 iterations took {t*1000:.3f}ms")
