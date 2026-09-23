"""
Empirical benchmark for Filling Bookcase Shelves Shelf Splitting
"""
import time
from algorithms.practice.dynamic_programming_1d.filling_bookcase_shelf import solve_filling_bookcase_shelf

def benchmark_filling_bookcase_shelf():
    start = time.perf_counter()
    for _ in range(100):
        solve_filling_bookcase_shelf([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_filling_bookcase_shelf()
    print(f"Filling Bookcase Shelves Shelf Splitting 100 iterations took {t*1000:.3f}ms")
