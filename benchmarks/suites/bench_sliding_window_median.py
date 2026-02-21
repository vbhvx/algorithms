"""
Empirical benchmark for Sliding Window Median Heaps
"""
import time
from algorithms.practice.sliding_window.sliding_window_median import solve_sliding_window_median

def benchmark_sliding_window_median():
    start = time.perf_counter()
    for _ in range(100):
        solve_sliding_window_median([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_sliding_window_median()
    print(f"Sliding Window Median Heaps 100 iterations took {t*1000:.3f}ms")
