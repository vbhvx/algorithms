"""
Empirical benchmark for Merge Sorted Array from End
"""
import time
from algorithms.practice.two_pointers.merge_sorted_array import solve_merge_sorted_array

def benchmark_merge_sorted_array():
    start = time.perf_counter()
    for _ in range(100):
        solve_merge_sorted_array([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_merge_sorted_array()
    print(f"Merge Sorted Array from End 100 iterations took {t*1000:.3f}ms")
