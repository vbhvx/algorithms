"""
Empirical benchmark for Count Nice Subarrays Exact K
"""
import time
from algorithms.practice.sliding_window.count_nice_subarrays import solve_count_nice_subarrays

def benchmark_count_nice_subarrays():
    start = time.perf_counter()
    for _ in range(100):
        solve_count_nice_subarrays([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_count_nice_subarrays()
    print(f"Count Nice Subarrays Exact K 100 iterations took {t*1000:.3f}ms")
