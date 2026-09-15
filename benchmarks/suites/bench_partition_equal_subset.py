"""
Empirical benchmark for Partition Equal Subset Sum 0-1 Knapsack
"""
import time
from algorithms.practice.dynamic_programming_1d.partition_equal_subset import solve_partition_equal_subset

def benchmark_partition_equal_subset():
    start = time.perf_counter()
    for _ in range(100):
        solve_partition_equal_subset([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_partition_equal_subset()
    print(f"Partition Equal Subset Sum 0-1 Knapsack 100 iterations took {t*1000:.3f}ms")
