"""
Empirical benchmark for Decode Ways Numeric String Split
"""
import time
from algorithms.practice.dynamic_programming_1d.decode_ways_1d import solve_decode_ways_1d

def benchmark_decode_ways_1d():
    start = time.perf_counter()
    for _ in range(100):
        solve_decode_ways_1d([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_decode_ways_1d()
    print(f"Decode Ways Numeric String Split 100 iterations took {t*1000:.3f}ms")
