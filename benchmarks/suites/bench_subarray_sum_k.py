"""
Empirical benchmark for Subarray Sum Equals K Prefix Map
"""
import time
from algorithms.practice.arrays_and_hashing.subarray_sum_k import solve_subarray_sum_k

def benchmark_subarray_sum_k():
    start = time.perf_counter()
    for _ in range(100):
        solve_subarray_sum_k([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_subarray_sum_k()
    print(f"Subarray Sum Equals K Prefix Map 100 iterations took {t*1000:.3f}ms")
