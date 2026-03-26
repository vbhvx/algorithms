"""
Empirical benchmark for Search in Rotated Sorted Array Duplicates
"""
import time
from algorithms.practice.binary_search.search_rotated_ii import solve_search_rotated_ii

def benchmark_search_rotated_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_search_rotated_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_search_rotated_ii()
    print(f"Search in Rotated Sorted Array Duplicates 100 iterations took {t*1000:.3f}ms")
