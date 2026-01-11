"""
Empirical benchmark for First Missing Positive In Place
"""
import time
from algorithms.practice.arrays_and_hashing.first_missing_positive import solve_first_missing_positive

def benchmark_first_missing_positive():
    start = time.perf_counter()
    for _ in range(100):
        solve_first_missing_positive([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_first_missing_positive()
    print(f"First Missing Positive In Place 100 iterations took {t*1000:.3f}ms")
