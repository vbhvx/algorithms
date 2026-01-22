"""
Empirical benchmark for Custom Sort String Frequency
"""
import time
from algorithms.practice.arrays_and_hashing.custom_sort_string import solve_custom_sort_string

def benchmark_custom_sort_string():
    start = time.perf_counter()
    for _ in range(100):
        solve_custom_sort_string([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_custom_sort_string()
    print(f"Custom Sort String Frequency 100 iterations took {t*1000:.3f}ms")
