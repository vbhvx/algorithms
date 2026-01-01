"""
Empirical benchmark for Two Sum Hash Map
"""
import time
from algorithms.practice.arrays_and_hashing.two_sum import solve_two_sum

def benchmark_two_sum():
    start = time.perf_counter()
    for _ in range(100):
        solve_two_sum([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_two_sum()
    print(f"Two Sum Hash Map 100 iterations took {t*1000:.3f}ms")
