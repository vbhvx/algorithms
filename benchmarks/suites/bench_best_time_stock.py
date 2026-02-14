"""
Empirical benchmark for Best Time Stock Running Min
"""
import time
from algorithms.practice.sliding_window.best_time_stock import solve_best_time_stock

def benchmark_best_time_stock():
    start = time.perf_counter()
    for _ in range(100):
        solve_best_time_stock([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_best_time_stock()
    print(f"Best Time Stock Running Min 100 iterations took {t*1000:.3f}ms")
