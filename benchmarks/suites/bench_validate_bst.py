"""
Empirical benchmark for Validate Binary Search Tree Inorder Range
"""
import time
from algorithms.practice.trees_and_bst.validate_bst import solve_validate_bst

def benchmark_validate_bst():
    start = time.perf_counter()
    for _ in range(100):
        solve_validate_bst([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_validate_bst()
    print(f"Validate Binary Search Tree Inorder Range 100 iterations took {t*1000:.3f}ms")
