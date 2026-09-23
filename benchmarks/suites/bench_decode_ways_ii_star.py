"""
Empirical benchmark for Decode Ways II Wildcard Digit Recurrence
"""
import time
from algorithms.practice.dynamic_programming_1d.decode_ways_ii_star import solve_decode_ways_ii_star

def benchmark_decode_ways_ii_star():
    start = time.perf_counter()
    for _ in range(100):
        solve_decode_ways_ii_star([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_decode_ways_ii_star()
    print(f"Decode Ways II Wildcard Digit Recurrence 100 iterations took {t*1000:.3f}ms")
