"""
Empirical benchmark for Combination Sum IV Permutation Sum
"""
import time
from algorithms.practice.dynamic_programming_1d.combination_sum_iv_dp import solve_combination_sum_iv_dp

def benchmark_combination_sum_iv_dp():
    start = time.perf_counter()
    for _ in range(100):
        solve_combination_sum_iv_dp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_combination_sum_iv_dp()
    print(f"Combination Sum IV Permutation Sum 100 iterations took {t*1000:.3f}ms")
