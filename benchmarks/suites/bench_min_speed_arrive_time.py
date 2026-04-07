"""
Empirical benchmark for Minimum Speed to Arrive on Time
"""
import time
from algorithms.practice.binary_search.min_speed_arrive_time import solve_min_speed_arrive_time

def benchmark_min_speed_arrive_time():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_speed_arrive_time([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_speed_arrive_time()
    print(f"Minimum Speed to Arrive on Time 100 iterations took {t*1000:.3f}ms")
