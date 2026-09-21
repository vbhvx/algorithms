"""
Empirical benchmark for Minimum Cost For Tickets 7 and 30 Days
"""
import time
from algorithms.practice.dynamic_programming_1d.min_cost_tickets import solve_min_cost_tickets

def benchmark_min_cost_tickets():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_cost_tickets([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_cost_tickets()
    print(f"Minimum Cost For Tickets 7 and 30 Days 100 iterations took {t*1000:.3f}ms")
