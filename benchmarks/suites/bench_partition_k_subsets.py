"""
Empirical benchmark for Partition to K Equal Sum Subsets Bitmask
"""
import time
from algorithms.practice.backtracking.partition_k_subsets import solve_partition_k_subsets

def benchmark_partition_k_subsets():
    start = time.perf_counter()
    for _ in range(100):
        solve_partition_k_subsets([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_partition_k_subsets()
    print(f"Partition to K Equal Sum Subsets Bitmask 100 iterations took {t*1000:.3f}ms")
