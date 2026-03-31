"""
Empirical benchmark for Capacity to Ship Packages within D Days
"""
import time
from algorithms.practice.binary_search.ship_packages_d_days import solve_ship_packages_d_days

def benchmark_ship_packages_d_days():
    start = time.perf_counter()
    for _ in range(100):
        solve_ship_packages_d_days([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_ship_packages_d_days()
    print(f"Capacity to Ship Packages within D Days 100 iterations took {t*1000:.3f}ms")
