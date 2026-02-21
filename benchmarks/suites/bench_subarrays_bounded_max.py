"""
Empirical benchmark for Subarrays with Bounded Maximum
"""
import time
from algorithms.practice.sliding_window.subarrays_bounded_max import solve_subarrays_bounded_max

def benchmark_subarrays_bounded_max():
    start = time.perf_counter()
    for _ in range(100):
        solve_subarrays_bounded_max([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_subarrays_bounded_max()
    print(f"Subarrays with Bounded Maximum 100 iterations took {t*1000:.3f}ms")
