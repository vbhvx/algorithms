"""
Empirical benchmark for Maximal Square Dynamic Programming
"""
import time
from algorithms.practice.dynamic_programming_2d.maximal_square_dp import solve_maximal_square_dp

def benchmark_maximal_square_dp():
    start = time.perf_counter()
    for _ in range(100):
        solve_maximal_square_dp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_maximal_square_dp()
    print(f"Maximal Square Dynamic Programming 100 iterations took {t*1000:.3f}ms")
