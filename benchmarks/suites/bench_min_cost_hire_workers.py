"""
Empirical benchmark for Minimum Cost to Hire K Workers Ratio Heap
"""
import time
from algorithms.practice.heaps_and_priority.min_cost_hire_workers import solve_min_cost_hire_workers

def benchmark_min_cost_hire_workers():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_cost_hire_workers([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_cost_hire_workers()
    print(f"Minimum Cost to Hire K Workers Ratio Heap 100 iterations took {t*1000:.3f}ms")
