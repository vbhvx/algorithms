"""
Empirical benchmark for Count Complete Subarrays In Array
"""
import time
from algorithms.practice.sliding_window.complete_subarrays import solve_complete_subarrays

def benchmark_complete_subarrays():
    start = time.perf_counter()
    for _ in range(100):
        solve_complete_subarrays([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_complete_subarrays()
    print(f"Count Complete Subarrays In Array 100 iterations took {t*1000:.3f}ms")
