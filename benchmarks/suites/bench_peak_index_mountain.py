"""
Empirical benchmark for Peak Index in a Mountain Array
"""
import time
from algorithms.practice.binary_search.peak_index_mountain import solve_peak_index_mountain

def benchmark_peak_index_mountain():
    start = time.perf_counter()
    for _ in range(100):
        solve_peak_index_mountain([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_peak_index_mountain()
    print(f"Peak Index in a Mountain Array 100 iterations took {t*1000:.3f}ms")
