"""
Empirical benchmark for Single Element in Sorted Array Parity
"""
import time
from algorithms.practice.binary_search.single_element_sorted import solve_single_element_sorted

def benchmark_single_element_sorted():
    start = time.perf_counter()
    for _ in range(100):
        solve_single_element_sorted([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_single_element_sorted()
    print(f"Single Element in Sorted Array Parity 100 iterations took {t*1000:.3f}ms")
