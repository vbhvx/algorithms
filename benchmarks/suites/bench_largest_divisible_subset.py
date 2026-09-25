"""
Empirical benchmark for Largest Divisible Subset Suffix Links
"""
import time
from algorithms.practice.dynamic_programming_1d.largest_divisible_subset import solve_largest_divisible_subset

def benchmark_largest_divisible_subset():
    start = time.perf_counter()
    for _ in range(100):
        solve_largest_divisible_subset([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_largest_divisible_subset()
    print(f"Largest Divisible Subset Suffix Links 100 iterations took {t*1000:.3f}ms")
