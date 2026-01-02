"""
Empirical benchmark for Product of Array Except Self
"""
import time
from algorithms.practice.arrays_and_hashing.product_except_self import solve_product_except_self

def benchmark_product_except_self():
    start = time.perf_counter()
    for _ in range(100):
        solve_product_except_self([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_product_except_self()
    print(f"Product of Array Except Self 100 iterations took {t*1000:.3f}ms")
