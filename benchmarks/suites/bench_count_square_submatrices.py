"""
Empirical benchmark for Count Square Submatrices with All Ones
"""
import time
from algorithms.practice.dynamic_programming_2d.count_square_submatrices import solve_count_square_submatrices

def benchmark_count_square_submatrices():
    start = time.perf_counter()
    for _ in range(100):
        solve_count_square_submatrices([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_count_square_submatrices()
    print(f"Count Square Submatrices with All Ones 100 iterations took {t*1000:.3f}ms")
