"""
Empirical benchmark for N-Queens II Total Solutions Count Bitmask
"""
import time
from algorithms.practice.backtracking.n_queens_ii_count import solve_n_queens_ii_count

def benchmark_n_queens_ii_count():
    start = time.perf_counter()
    for _ in range(100):
        solve_n_queens_ii_count([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_n_queens_ii_count()
    print(f"N-Queens II Total Solutions Count Bitmask 100 iterations took {t*1000:.3f}ms")
