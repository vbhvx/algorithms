"""
Empirical benchmark for Min Cost Climbing Stairs Recurrence
"""
import time
from algorithms.practice.dynamic_programming_1d.min_cost_climbing import solve_min_cost_climbing

def benchmark_min_cost_climbing():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_cost_climbing([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_cost_climbing()
    print(f"Min Cost Climbing Stairs Recurrence 100 iterations took {t*1000:.3f}ms")
