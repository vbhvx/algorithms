"""
Empirical benchmark for Brick Wall Minimum Cross Cuts
"""
import time
from algorithms.practice.arrays_and_hashing.brick_wall import solve_brick_wall

def benchmark_brick_wall():
    start = time.perf_counter()
    for _ in range(100):
        solve_brick_wall([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_brick_wall()
    print(f"Brick Wall Minimum Cross Cuts 100 iterations took {t*1000:.3f}ms")
