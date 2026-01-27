"""
Empirical benchmark for Two Sum II Sorted Pointers
"""
import time
from algorithms.practice.two_pointers.two_sum_sorted import solve_two_sum_sorted

def benchmark_two_sum_sorted():
    start = time.perf_counter()
    for _ in range(100):
        solve_two_sum_sorted([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_two_sum_sorted()
    print(f"Two Sum II Sorted Pointers 100 iterations took {t*1000:.3f}ms")
