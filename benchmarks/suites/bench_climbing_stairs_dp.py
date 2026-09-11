"""
Empirical benchmark for Climbing Stairs Fibonacci Memory Array
"""
import time
from algorithms.practice.dynamic_programming_1d.climbing_stairs_dp import solve_climbing_stairs_dp

def benchmark_climbing_stairs_dp():
    start = time.perf_counter()
    for _ in range(100):
        solve_climbing_stairs_dp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_climbing_stairs_dp()
    print(f"Climbing Stairs Fibonacci Memory Array 100 iterations took {t*1000:.3f}ms")
