"""
Empirical benchmark for Daily Temperatures Monotonic Stack
"""
import time
from algorithms.practice.stack_and_queue.daily_temperatures import solve_daily_temperatures

def benchmark_daily_temperatures():
    start = time.perf_counter()
    for _ in range(100):
        solve_daily_temperatures([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_daily_temperatures()
    print(f"Daily Temperatures Monotonic Stack 100 iterations took {t*1000:.3f}ms")
