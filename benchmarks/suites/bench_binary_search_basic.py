"""
Empirical benchmark for Binary Search Standard Recursive Iterative
"""
import time
from algorithms.practice.binary_search.binary_search_basic import solve_binary_search_basic

def benchmark_binary_search_basic():
    start = time.perf_counter()
    for _ in range(100):
        solve_binary_search_basic([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_binary_search_basic()
    print(f"Binary Search Standard Recursive Iterative 100 iterations took {t*1000:.3f}ms")
