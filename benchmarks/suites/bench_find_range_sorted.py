"""
Empirical benchmark for Find First and Last Position in Sorted Array
"""
import time
from algorithms.practice.binary_search.find_range_sorted import solve_find_range_sorted

def benchmark_find_range_sorted():
    start = time.perf_counter()
    for _ in range(100):
        solve_find_range_sorted([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_find_range_sorted()
    print(f"Find First and Last Position in Sorted Array 100 iterations took {t*1000:.3f}ms")
