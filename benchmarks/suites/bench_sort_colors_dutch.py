"""
Empirical benchmark for Sort Colors Dutch National Flag
"""
import time
from algorithms.practice.two_pointers.sort_colors_dutch import solve_sort_colors_dutch

def benchmark_sort_colors_dutch():
    start = time.perf_counter()
    for _ in range(100):
        solve_sort_colors_dutch([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_sort_colors_dutch()
    print(f"Sort Colors Dutch National Flag 100 iterations took {t*1000:.3f}ms")
