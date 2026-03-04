"""
Empirical benchmark for Minimum Operations Reduce X to Zero
"""
import time
from algorithms.practice.sliding_window.min_ops_reduce_x import solve_min_ops_reduce_x

def benchmark_min_ops_reduce_x():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_ops_reduce_x([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_ops_reduce_x()
    print(f"Minimum Operations Reduce X to Zero 100 iterations took {t*1000:.3f}ms")
