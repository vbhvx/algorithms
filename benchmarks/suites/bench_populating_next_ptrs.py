"""
Empirical benchmark for Populating Next Right Pointers Perfect Tree
"""
import time
from algorithms.practice.trees_and_bst.populating_next_ptrs import solve_populating_next_ptrs

def benchmark_populating_next_ptrs():
    start = time.perf_counter()
    for _ in range(100):
        solve_populating_next_ptrs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_populating_next_ptrs()
    print(f"Populating Next Right Pointers Perfect Tree 100 iterations took {t*1000:.3f}ms")
