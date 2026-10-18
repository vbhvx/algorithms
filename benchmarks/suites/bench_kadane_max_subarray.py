"""
Empirical benchmark for Maximum Subarray Kadane Running Sum
"""
import time
from algorithms.practice.greedy_algorithms.kadane_max_subarray import solve_kadane_max_subarray

def benchmark_kadane_max_subarray():
    start = time.perf_counter()
    for _ in range(100):
        solve_kadane_max_subarray([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kadane_max_subarray()
    print(f"Maximum Subarray Kadane Running Sum 100 iterations took {t*1000:.3f}ms")
