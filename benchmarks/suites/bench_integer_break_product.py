"""
Empirical benchmark for Integer Break Maximum Product Factor
"""
import time
from algorithms.practice.dynamic_programming_1d.integer_break_product import solve_integer_break_product

def benchmark_integer_break_product():
    start = time.perf_counter()
    for _ in range(100):
        solve_integer_break_product([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_integer_break_product()
    print(f"Integer Break Maximum Product Factor 100 iterations took {t*1000:.3f}ms")
