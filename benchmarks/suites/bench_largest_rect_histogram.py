"""
Empirical benchmark for Largest Rectangle in Histogram
"""
import time
from algorithms.practice.stack_and_queue.largest_rect_histogram import solve_largest_rect_histogram

def benchmark_largest_rect_histogram():
    start = time.perf_counter()
    for _ in range(100):
        solve_largest_rect_histogram([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_largest_rect_histogram()
    print(f"Largest Rectangle in Histogram 100 iterations took {t*1000:.3f}ms")
