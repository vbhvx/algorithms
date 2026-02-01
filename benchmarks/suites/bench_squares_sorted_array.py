"""
Empirical benchmark for Squares of Sorted Array
"""
import time
from algorithms.practice.two_pointers.squares_sorted_array import solve_squares_sorted_array

def benchmark_squares_sorted_array():
    start = time.perf_counter()
    for _ in range(100):
        solve_squares_sorted_array([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_squares_sorted_array()
    print(f"Squares of Sorted Array 100 iterations took {t*1000:.3f}ms")
