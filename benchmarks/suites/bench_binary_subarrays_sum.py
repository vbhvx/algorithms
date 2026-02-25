"""
Empirical benchmark for Binary Subarrays With Sum Window
"""
import time
from algorithms.practice.sliding_window.binary_subarrays_sum import solve_binary_subarrays_sum

def benchmark_binary_subarrays_sum():
    start = time.perf_counter()
    for _ in range(100):
        solve_binary_subarrays_sum([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_binary_subarrays_sum()
    print(f"Binary Subarrays With Sum Window 100 iterations took {t*1000:.3f}ms")
