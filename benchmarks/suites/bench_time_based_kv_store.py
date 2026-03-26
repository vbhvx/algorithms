"""
Empirical benchmark for Time Based Key-Value Store Bisect
"""
import time
from algorithms.practice.binary_search.time_based_kv_store import solve_time_based_kv_store

def benchmark_time_based_kv_store():
    start = time.perf_counter()
    for _ in range(100):
        solve_time_based_kv_store([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_time_based_kv_store()
    print(f"Time Based Key-Value Store Bisect 100 iterations took {t*1000:.3f}ms")
