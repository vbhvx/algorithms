"""
Empirical benchmark for Paint Fence K Colors Same Adjacent
"""
import time
from algorithms.practice.dynamic_programming_2d.paint_fence_combinations import solve_paint_fence_combinations

def benchmark_paint_fence_combinations():
    start = time.perf_counter()
    for _ in range(100):
        solve_paint_fence_combinations([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_paint_fence_combinations()
    print(f"Paint Fence K Colors Same Adjacent 100 iterations took {t*1000:.3f}ms")
