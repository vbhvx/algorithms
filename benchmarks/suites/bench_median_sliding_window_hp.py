"""
Empirical benchmark for Median Sliding Window Dual Heaps Lazy Deletion
"""
import time
from algorithms.practice.heaps_and_priority.median_sliding_window_hp import solve_median_sliding_window_hp

def benchmark_median_sliding_window_hp():
    start = time.perf_counter()
    for _ in range(100):
        solve_median_sliding_window_hp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_median_sliding_window_hp()
    print(f"Median Sliding Window Dual Heaps Lazy Deletion 100 iterations took {t*1000:.3f}ms")
