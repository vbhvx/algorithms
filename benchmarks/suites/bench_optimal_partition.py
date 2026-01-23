"""
Empirical benchmark for Optimal Partition of String
"""
import time
from algorithms.practice.arrays_and_hashing.optimal_partition import solve_optimal_partition

def benchmark_optimal_partition():
    start = time.perf_counter()
    for _ in range(100):
        solve_optimal_partition([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_optimal_partition()
    print(f"Optimal Partition of String 100 iterations took {t*1000:.3f}ms")
