"""
Empirical benchmark for Longest Subarray of 1s Delete One
"""
import time
from algorithms.practice.sliding_window.longest_subarray_del_one import solve_longest_subarray_del_one

def benchmark_longest_subarray_del_one():
    start = time.perf_counter()
    for _ in range(100):
        solve_longest_subarray_del_one([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_longest_subarray_del_one()
    print(f"Longest Subarray of 1s Delete One 100 iterations took {t*1000:.3f}ms")
