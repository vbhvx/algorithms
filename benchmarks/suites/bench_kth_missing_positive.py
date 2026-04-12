"""
Empirical benchmark for Kth Missing Positive Number Bisect
"""
import time
from algorithms.practice.binary_search.kth_missing_positive import solve_kth_missing_positive

def benchmark_kth_missing_positive():
    start = time.perf_counter()
    for _ in range(100):
        solve_kth_missing_positive([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kth_missing_positive()
    print(f"Kth Missing Positive Number Bisect 100 iterations took {t*1000:.3f}ms")
