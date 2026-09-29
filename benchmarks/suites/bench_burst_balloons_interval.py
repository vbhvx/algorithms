"""
Empirical benchmark for Burst Balloons Interval Dynamic Programming
"""
import time
from algorithms.practice.dynamic_programming_2d.burst_balloons_interval import solve_burst_balloons_interval

def benchmark_burst_balloons_interval():
    start = time.perf_counter()
    for _ in range(100):
        solve_burst_balloons_interval([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_burst_balloons_interval()
    print(f"Burst Balloons Interval Dynamic Programming 100 iterations took {t*1000:.3f}ms")
