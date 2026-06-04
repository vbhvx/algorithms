"""
Empirical benchmark for Recover Binary Search Tree Morris Inorder
"""
import time
from algorithms.practice.trees_and_bst.recover_bst import solve_recover_bst

def benchmark_recover_bst():
    start = time.perf_counter()
    for _ in range(100):
        solve_recover_bst([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_recover_bst()
    print(f"Recover Binary Search Tree Morris Inorder 100 iterations took {t*1000:.3f}ms")
