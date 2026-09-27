"""
Empirical benchmark for Target Sum 0-1 Subset Partition
"""
import time
from algorithms.practice.dynamic_programming_2d.target_sum_subset_dp import solve_target_sum_subset_dp

def benchmark_target_sum_subset_dp():
    start = time.perf_counter()
    for _ in range(100):
        solve_target_sum_subset_dp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_target_sum_subset_dp()
    print(f"Target Sum 0-1 Subset Partition 100 iterations took {t*1000:.3f}ms")
