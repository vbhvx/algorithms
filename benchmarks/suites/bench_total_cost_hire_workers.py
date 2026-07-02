"""
Empirical benchmark for Total Cost to Hire K Workers Dual Heaps
"""
import time
from algorithms.practice.heaps_and_priority.total_cost_hire_workers import solve_total_cost_hire_workers

def benchmark_total_cost_hire_workers():
    start = time.perf_counter()
    for _ in range(100):
        solve_total_cost_hire_workers([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_total_cost_hire_workers()
    print(f"Total Cost to Hire K Workers Dual Heaps 100 iterations took {t*1000:.3f}ms")
