"""
Empirical benchmark for Partition to K Equal Subsets Bitmask Memo
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.partition_k_subsets_bm import solve_partition_k_subsets_bm

def benchmark_partition_k_subsets_bm():
    start = time.perf_counter()
    for _ in range(100):
        solve_partition_k_subsets_bm([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_partition_k_subsets_bm()
    print(f"Partition to K Equal Subsets Bitmask Memo 100 iterations took {t*1000:.3f}ms")
