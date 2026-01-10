"""
Empirical benchmark for Subarray Sums Divisible by K
"""
import time
from algorithms.practice.arrays_and_hashing.subarray_divisible_k import solve_subarray_divisible_k

def benchmark_subarray_divisible_k():
    start = time.perf_counter()
    for _ in range(100):
        solve_subarray_divisible_k([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_subarray_divisible_k()
    print(f"Subarray Sums Divisible by K 100 iterations took {t*1000:.3f}ms")
