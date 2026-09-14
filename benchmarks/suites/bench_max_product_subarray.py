"""
Empirical benchmark for Maximum Product Subarray Min Max Bounds
"""
import time
from algorithms.practice.dynamic_programming_1d.max_product_subarray import solve_max_product_subarray

def benchmark_max_product_subarray():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_product_subarray([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_product_subarray()
    print(f"Maximum Product Subarray Min Max Bounds 100 iterations took {t*1000:.3f}ms")
