"""
Empirical benchmark for Max Consecutive Ones III K Flips
"""
import time
from algorithms.practice.sliding_window.max_consecutive_ones_iii import solve_max_consecutive_ones_iii

def benchmark_max_consecutive_ones_iii():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_consecutive_ones_iii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_consecutive_ones_iii()
    print(f"Max Consecutive Ones III K Flips 100 iterations took {t*1000:.3f}ms")
