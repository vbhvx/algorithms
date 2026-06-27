"""
Empirical benchmark for Find Median from Data Stream Dual Heaps
"""
import time
from algorithms.practice.heaps_and_priority.find_median_stream import solve_find_median_stream

def benchmark_find_median_stream():
    start = time.perf_counter()
    for _ in range(100):
        solve_find_median_stream([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_find_median_stream()
    print(f"Find Median from Data Stream Dual Heaps 100 iterations took {t*1000:.3f}ms")
