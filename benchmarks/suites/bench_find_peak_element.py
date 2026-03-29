"""
Empirical benchmark for Find Peak Element Logarithmic Ascent
"""
import time
from algorithms.practice.binary_search.find_peak_element import solve_find_peak_element

def benchmark_find_peak_element():
    start = time.perf_counter()
    for _ in range(100):
        solve_find_peak_element([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_find_peak_element()
    print(f"Find Peak Element Logarithmic Ascent 100 iterations took {t*1000:.3f}ms")
