"""
Empirical benchmark for Ugly Number III Inclusion Exclusion
"""
import time
from algorithms.practice.binary_search.ugly_number_iii import solve_ugly_number_iii

def benchmark_ugly_number_iii():
    start = time.perf_counter()
    for _ in range(100):
        solve_ugly_number_iii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_ugly_number_iii()
    print(f"Ugly Number III Inclusion Exclusion 100 iterations took {t*1000:.3f}ms")
