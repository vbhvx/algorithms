"""
Empirical benchmark for H-Index II Sorted Citation Array
"""
import time
from algorithms.practice.binary_search.h_index_ii import solve_h_index_ii

def benchmark_h_index_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_h_index_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_h_index_ii()
    print(f"H-Index II Sorted Citation Array 100 iterations took {t*1000:.3f}ms")
