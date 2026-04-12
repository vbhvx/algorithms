"""
Empirical benchmark for Kth Smallest Number in Multiplication Table
"""
import time
from algorithms.practice.binary_search.kth_smallest_matrix import solve_kth_smallest_matrix

def benchmark_kth_smallest_matrix():
    start = time.perf_counter()
    for _ in range(100):
        solve_kth_smallest_matrix([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kth_smallest_matrix()
    print(f"Kth Smallest Number in Multiplication Table 100 iterations took {t*1000:.3f}ms")
