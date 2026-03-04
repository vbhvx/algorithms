"""
Empirical benchmark for Shortest Subarray Sum at Least K
"""
import time
from algorithms.practice.sliding_window.shortest_subarray_sum_k import solve_shortest_subarray_sum_k

def benchmark_shortest_subarray_sum_k():
    start = time.perf_counter()
    for _ in range(100):
        solve_shortest_subarray_sum_k([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_shortest_subarray_sum_k()
    print(f"Shortest Subarray Sum at Least K 100 iterations took {t*1000:.3f}ms")
