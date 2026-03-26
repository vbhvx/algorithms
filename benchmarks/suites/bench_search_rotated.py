"""
Empirical benchmark for Search in Rotated Sorted Array
"""
import time
from algorithms.practice.binary_search.search_rotated import solve_search_rotated

def benchmark_search_rotated():
    start = time.perf_counter()
    for _ in range(100):
        solve_search_rotated([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_search_rotated()
    print(f"Search in Rotated Sorted Array 100 iterations took {t*1000:.3f}ms")
