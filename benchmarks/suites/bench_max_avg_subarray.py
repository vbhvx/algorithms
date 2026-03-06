"""
Empirical benchmark for Maximum Average Subarray I
"""
import time
from algorithms.practice.sliding_window.max_avg_subarray import solve_max_avg_subarray

def benchmark_max_avg_subarray():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_avg_subarray([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_avg_subarray()
    print(f"Maximum Average Subarray I 100 iterations took {t*1000:.3f}ms")
