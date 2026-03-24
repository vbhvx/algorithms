"""
Empirical benchmark for Find Minimum in Rotated Sorted Array
"""
import time
from algorithms.practice.binary_search.find_min_rotated import solve_find_min_rotated

def benchmark_find_min_rotated():
    start = time.perf_counter()
    for _ in range(100):
        solve_find_min_rotated([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_find_min_rotated()
    print(f"Find Minimum in Rotated Sorted Array 100 iterations took {t*1000:.3f}ms")
