"""
Empirical benchmark for Paint House 3 Colors Adjacent Cost
"""
import time
from algorithms.practice.dynamic_programming_1d.paint_house_colors import solve_paint_house_colors

def benchmark_paint_house_colors():
    start = time.perf_counter()
    for _ in range(100):
        solve_paint_house_colors([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_paint_house_colors()
    print(f"Paint House 3 Colors Adjacent Cost 100 iterations took {t*1000:.3f}ms")
