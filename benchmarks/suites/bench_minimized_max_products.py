"""
Empirical benchmark for Minimized Maximum of Products in Stores
"""
import time
from algorithms.practice.binary_search.minimized_max_products import solve_minimized_max_products

def benchmark_minimized_max_products():
    start = time.perf_counter()
    for _ in range(100):
        solve_minimized_max_products([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_minimized_max_products()
    print(f"Minimized Maximum of Products in Stores 100 iterations took {t*1000:.3f}ms")
