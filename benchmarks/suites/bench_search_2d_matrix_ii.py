"""
Empirical benchmark for Search a 2D Matrix II Top Right Step
"""
import time
from algorithms.practice.binary_search.search_2d_matrix_ii import solve_search_2d_matrix_ii

def benchmark_search_2d_matrix_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_search_2d_matrix_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_search_2d_matrix_ii()
    print(f"Search a 2D Matrix II Top Right Step 100 iterations took {t*1000:.3f}ms")
