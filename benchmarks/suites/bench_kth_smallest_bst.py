"""
Empirical benchmark for Kth Smallest Element in BST Inorder
"""
import time
from algorithms.practice.trees_and_bst.kth_smallest_bst import solve_kth_smallest_bst

def benchmark_kth_smallest_bst():
    start = time.perf_counter()
    for _ in range(100):
        solve_kth_smallest_bst([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kth_smallest_bst()
    print(f"Kth Smallest Element in BST Inorder 100 iterations took {t*1000:.3f}ms")
