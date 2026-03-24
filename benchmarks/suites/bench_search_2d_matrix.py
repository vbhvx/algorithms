"""
Empirical benchmark for Search a 2D Matrix Virtual Index
"""
import time
from algorithms.practice.binary_search.search_2d_matrix import solve_search_2d_matrix

def benchmark_search_2d_matrix():
    start = time.perf_counter()
    for _ in range(100):
        solve_search_2d_matrix([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_search_2d_matrix()
    print(f"Search a 2D Matrix Virtual Index 100 iterations took {t*1000:.3f}ms")
