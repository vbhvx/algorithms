"""
Empirical benchmark for Numbers At Most N Given Digit Set Digit DP
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.numbers_at_most_n_digit import solve_numbers_at_most_n_digit

def benchmark_numbers_at_most_n_digit():
    start = time.perf_counter()
    for _ in range(100):
        solve_numbers_at_most_n_digit([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_numbers_at_most_n_digit()
    print(f"Numbers At Most N Given Digit Set Digit DP 100 iterations took {t*1000:.3f}ms")
