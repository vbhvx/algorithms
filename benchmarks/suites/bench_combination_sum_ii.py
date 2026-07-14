"""
Empirical benchmark for Combination Sum II Single Use Duplicates
"""
import time
from algorithms.practice.backtracking.combination_sum_ii import solve_combination_sum_ii

def benchmark_combination_sum_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_combination_sum_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_combination_sum_ii()
    print(f"Combination Sum II Single Use Duplicates 100 iterations took {t*1000:.3f}ms")
