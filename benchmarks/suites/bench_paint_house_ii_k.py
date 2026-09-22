"""
Empirical benchmark for Paint House II K Colors Running Min
"""
import time
from algorithms.practice.dynamic_programming_1d.paint_house_ii_k import solve_paint_house_ii_k

def benchmark_paint_house_ii_k():
    start = time.perf_counter()
    for _ in range(100):
        solve_paint_house_ii_k([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_paint_house_ii_k()
    print(f"Paint House II K Colors Running Min 100 iterations took {t*1000:.3f}ms")
