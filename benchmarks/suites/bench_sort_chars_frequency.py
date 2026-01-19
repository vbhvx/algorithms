"""
Empirical benchmark for Sort Characters by Frequency
"""
import time
from algorithms.practice.arrays_and_hashing.sort_chars_frequency import solve_sort_chars_frequency

def benchmark_sort_chars_frequency():
    start = time.perf_counter()
    for _ in range(100):
        solve_sort_chars_frequency([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_sort_chars_frequency()
    print(f"Sort Characters by Frequency 100 iterations took {t*1000:.3f}ms")
