"""
Empirical benchmark for Combination Sum III K Numbers Sum to N
"""
import time
from algorithms.practice.backtracking.combination_sum_iii import solve_combination_sum_iii

def benchmark_combination_sum_iii():
    start = time.perf_counter()
    for _ in range(100):
        solve_combination_sum_iii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_combination_sum_iii()
    print(f"Combination Sum III K Numbers Sum to N 100 iterations took {t*1000:.3f}ms")
