"""
Empirical benchmark for Palindrome Partitioning II Minimum Cuts
"""
import time
from algorithms.practice.dynamic_programming_2d.palindrome_partition_ii import solve_palindrome_partition_ii

def benchmark_palindrome_partition_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_palindrome_partition_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_palindrome_partition_ii()
    print(f"Palindrome Partitioning II Minimum Cuts 100 iterations took {t*1000:.3f}ms")
