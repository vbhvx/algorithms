"""
Empirical benchmark for Hungarian Method Kuhn-Munkres Assignment
"""
import time
from algorithms.practice.network_flow_matching.hungarian_assignment import solve_hungarian_assignment

def benchmark_hungarian_assignment():
    start = time.perf_counter()
    for _ in range(100):
        solve_hungarian_assignment([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_hungarian_assignment()
    print(f"Hungarian Method Kuhn-Munkres Assignment 100 iterations took {t*1000:.3f}ms")
