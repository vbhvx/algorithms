"""
Empirical benchmark for Populating Next Right Pointers II Any Tree
"""
import time
from algorithms.practice.trees_and_bst.populating_next_ii import solve_populating_next_ii

def benchmark_populating_next_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_populating_next_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_populating_next_ii()
    print(f"Populating Next Right Pointers II Any Tree 100 iterations took {t*1000:.3f}ms")
