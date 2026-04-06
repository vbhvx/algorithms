"""
Empirical benchmark for Sqrt X Integer Floor Binary Search
"""
import time
from algorithms.practice.binary_search.sqrt_x_binary_search import solve_sqrt_x_binary_search

def benchmark_sqrt_x_binary_search():
    start = time.perf_counter()
    for _ in range(100):
        solve_sqrt_x_binary_search([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_sqrt_x_binary_search()
    print(f"Sqrt X Integer Floor Binary Search 100 iterations took {t*1000:.3f}ms")
