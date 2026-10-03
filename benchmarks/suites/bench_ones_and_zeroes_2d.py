"""
Empirical benchmark for Ones and Zeroes 2D Knapsack Capacity
"""
import time
from algorithms.practice.dynamic_programming_2d.ones_and_zeroes_2d import solve_ones_and_zeroes_2d

def benchmark_ones_and_zeroes_2d():
    start = time.perf_counter()
    for _ in range(100):
        solve_ones_and_zeroes_2d([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_ones_and_zeroes_2d()
    print(f"Ones and Zeroes 2D Knapsack Capacity 100 iterations took {t*1000:.3f}ms")
