"""
Empirical benchmark for Minimum Recolors K Consecutive Black
"""
import time
from algorithms.practice.sliding_window.min_recolors_black import solve_min_recolors_black

def benchmark_min_recolors_black():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_recolors_black([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_recolors_black()
    print(f"Minimum Recolors K Consecutive Black 100 iterations took {t*1000:.3f}ms")
