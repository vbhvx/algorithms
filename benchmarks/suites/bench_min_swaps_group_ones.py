"""
Empirical benchmark for Minimum Swaps Group All Ones
"""
import time
from algorithms.practice.sliding_window.min_swaps_group_ones import solve_min_swaps_group_ones

def benchmark_min_swaps_group_ones():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_swaps_group_ones([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_swaps_group_ones()
    print(f"Minimum Swaps Group All Ones 100 iterations took {t*1000:.3f}ms")
