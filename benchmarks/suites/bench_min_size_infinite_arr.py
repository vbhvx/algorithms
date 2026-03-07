"""
Empirical benchmark for Minimum Size Subarray Infinite Array
"""
import time
from algorithms.practice.sliding_window.min_size_infinite_arr import solve_min_size_infinite_arr

def benchmark_min_size_infinite_arr():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_size_infinite_arr([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_size_infinite_arr()
    print(f"Minimum Size Subarray Infinite Array 100 iterations took {t*1000:.3f}ms")
