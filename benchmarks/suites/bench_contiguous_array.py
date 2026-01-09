"""
Empirical benchmark for Contiguous Array Equal 0 1
"""
import time
from algorithms.practice.arrays_and_hashing.contiguous_array import solve_contiguous_array

def benchmark_contiguous_array():
    start = time.perf_counter()
    for _ in range(100):
        solve_contiguous_array([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_contiguous_array()
    print(f"Contiguous Array Equal 0 1 100 iterations took {t*1000:.3f}ms")
