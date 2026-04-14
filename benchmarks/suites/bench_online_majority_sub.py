"""
Empirical benchmark for Online Majority Element In Subarray
"""
import time
from algorithms.practice.binary_search.online_majority_sub import solve_online_majority_sub

def benchmark_online_majority_sub():
    start = time.perf_counter()
    for _ in range(100):
        solve_online_majority_sub([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_online_majority_sub()
    print(f"Online Majority Element In Subarray 100 iterations took {t*1000:.3f}ms")
