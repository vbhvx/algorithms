"""
Empirical benchmark for Domino and Tromino Tiling Recurrence Matrix
"""
import time
from algorithms.practice.dynamic_programming_1d.domino_tromino_tiling import solve_domino_tromino_tiling

def benchmark_domino_tromino_tiling():
    start = time.perf_counter()
    for _ in range(100):
        solve_domino_tromino_tiling([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_domino_tromino_tiling()
    print(f"Domino and Tromino Tiling Recurrence Matrix 100 iterations took {t*1000:.3f}ms")
