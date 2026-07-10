"""
Empirical benchmark for Find Kth Smallest Element in Sorted Ranges
"""
import time
from algorithms.practice.heaps_and_priority.kth_smallest_ranges import solve_kth_smallest_ranges

def benchmark_kth_smallest_ranges():
    start = time.perf_counter()
    for _ in range(100):
        solve_kth_smallest_ranges([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kth_smallest_ranges()
    print(f"Find Kth Smallest Element in Sorted Ranges 100 iterations took {t*1000:.3f}ms")
