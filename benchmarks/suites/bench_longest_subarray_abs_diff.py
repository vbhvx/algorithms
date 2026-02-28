"""
Empirical benchmark for Longest Subarray Absolute Diff Limit
"""
import time
from algorithms.practice.sliding_window.longest_subarray_abs_diff import solve_longest_subarray_abs_diff

def benchmark_longest_subarray_abs_diff():
    start = time.perf_counter()
    for _ in range(100):
        solve_longest_subarray_abs_diff([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_longest_subarray_abs_diff()
    print(f"Longest Subarray Absolute Diff Limit 100 iterations took {t*1000:.3f}ms")
