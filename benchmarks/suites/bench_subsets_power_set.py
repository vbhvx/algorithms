"""
Empirical benchmark for Subsets Power Set Recursive Backtracking
"""
import time
from algorithms.practice.backtracking.subsets_power_set import solve_subsets_power_set

def benchmark_subsets_power_set():
    start = time.perf_counter()
    for _ in range(100):
        solve_subsets_power_set([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_subsets_power_set()
    print(f"Subsets Power Set Recursive Backtracking 100 iterations took {t*1000:.3f}ms")
