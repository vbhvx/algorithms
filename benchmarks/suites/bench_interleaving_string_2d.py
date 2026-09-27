"""
Empirical benchmark for Interleaving String 2D Boolean Table
"""
import time
from algorithms.practice.dynamic_programming_2d.interleaving_string_2d import solve_interleaving_string_2d

def benchmark_interleaving_string_2d():
    start = time.perf_counter()
    for _ in range(100):
        solve_interleaving_string_2d([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_interleaving_string_2d()
    print(f"Interleaving String 2D Boolean Table 100 iterations took {t*1000:.3f}ms")
