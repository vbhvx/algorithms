"""
Empirical benchmark for Reduce Array Size to The Half Frequency Greed
"""
import time
from algorithms.practice.greedy_algorithms.reduce_array_half import solve_reduce_array_half

def benchmark_reduce_array_half():
    start = time.perf_counter()
    for _ in range(100):
        solve_reduce_array_half([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reduce_array_half()
    print(f"Reduce Array Size to The Half Frequency Greed 100 iterations took {t*1000:.3f}ms")
