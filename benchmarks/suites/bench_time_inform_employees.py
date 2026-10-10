"""
Empirical benchmark for Time Needed to Inform All Employees Tree DP
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.time_inform_employees import solve_time_inform_employees

def benchmark_time_inform_employees():
    start = time.perf_counter()
    for _ in range(100):
        solve_time_inform_employees([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_time_inform_employees()
    print(f"Time Needed to Inform All Employees Tree DP 100 iterations took {t*1000:.3f}ms")
