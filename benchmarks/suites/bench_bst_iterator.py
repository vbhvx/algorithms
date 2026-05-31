"""
Empirical benchmark for Binary Search Tree Iterator Controlled Stack
"""
import time
from algorithms.practice.trees_and_bst.bst_iterator import solve_bst_iterator

def benchmark_bst_iterator():
    start = time.perf_counter()
    for _ in range(100):
        solve_bst_iterator([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_bst_iterator()
    print(f"Binary Search Tree Iterator Controlled Stack 100 iterations took {t*1000:.3f}ms")
