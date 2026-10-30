"""
Empirical benchmark for Employee Free Time All Work Intervals Sweep
"""
import time
from algorithms.practice.intervals_scheduling.employee_free_time import solve_employee_free_time

def benchmark_employee_free_time():
    start = time.perf_counter()
    for _ in range(100):
        solve_employee_free_time([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_employee_free_time()
    print(f"Employee Free Time All Work Intervals Sweep 100 iterations took {t*1000:.3f}ms")
