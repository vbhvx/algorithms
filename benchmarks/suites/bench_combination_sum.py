"""
Empirical benchmark for Combination Sum Unlimited Candidates
"""
import time
from algorithms.practice.backtracking.combination_sum import solve_combination_sum

def benchmark_combination_sum():
    start = time.perf_counter()
    for _ in range(100):
        solve_combination_sum([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_combination_sum()
    print(f"Combination Sum Unlimited Candidates 100 iterations took {t*1000:.3f}ms")
