"""
Empirical benchmark for Unique Binary Search Trees II Tree Generation
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.unique_bst_ii_generate import solve_unique_bst_ii_generate

def benchmark_unique_bst_ii_generate():
    start = time.perf_counter()
    for _ in range(100):
        solve_unique_bst_ii_generate([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_unique_bst_ii_generate()
    print(f"Unique Binary Search Trees II Tree Generation 100 iterations took {t*1000:.3f}ms")
