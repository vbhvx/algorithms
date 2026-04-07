"""
Empirical benchmark for Find Smallest Divisor Given Threshold
"""
import time
from algorithms.practice.binary_search.smallest_divisor_thresh import solve_smallest_divisor_thresh

def benchmark_smallest_divisor_thresh():
    start = time.perf_counter()
    for _ in range(100):
        solve_smallest_divisor_thresh([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_smallest_divisor_thresh()
    print(f"Find Smallest Divisor Given Threshold 100 iterations took {t*1000:.3f}ms")
