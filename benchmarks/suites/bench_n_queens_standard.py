"""
Empirical benchmark for N-Queens Board Backtracking Diagonal Bitmask
"""
import time
from algorithms.practice.backtracking.n_queens_standard import solve_n_queens_standard

def benchmark_n_queens_standard():
    start = time.perf_counter()
    for _ in range(100):
        solve_n_queens_standard([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_n_queens_standard()
    print(f"N-Queens Board Backtracking Diagonal Bitmask 100 iterations took {t*1000:.3f}ms")
