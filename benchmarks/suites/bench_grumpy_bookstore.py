"""
Empirical benchmark for Grumpy Bookstore Owner Window
"""
import time
from algorithms.practice.sliding_window.grumpy_bookstore import solve_grumpy_bookstore

def benchmark_grumpy_bookstore():
    start = time.perf_counter()
    for _ in range(100):
        solve_grumpy_bookstore([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_grumpy_bookstore()
    print(f"Grumpy Bookstore Owner Window 100 iterations took {t*1000:.3f}ms")
