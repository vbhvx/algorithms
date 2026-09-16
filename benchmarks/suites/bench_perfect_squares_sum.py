"""
Empirical benchmark for Perfect Squares Lagrange Four Square Theorem
"""
import time
from algorithms.practice.dynamic_programming_1d.perfect_squares_sum import solve_perfect_squares_sum

def benchmark_perfect_squares_sum():
    start = time.perf_counter()
    for _ in range(100):
        solve_perfect_squares_sum([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_perfect_squares_sum()
    print(f"Perfect Squares Lagrange Four Square Theorem 100 iterations took {t*1000:.3f}ms")
