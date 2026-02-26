"""
Empirical benchmark for Max Points You Can Obtain from Cards
"""
import time
from algorithms.practice.sliding_window.max_points_cards import solve_max_points_cards

def benchmark_max_points_cards():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_points_cards([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_points_cards()
    print(f"Max Points You Can Obtain from Cards 100 iterations took {t*1000:.3f}ms")
