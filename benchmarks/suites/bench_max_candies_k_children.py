"""
Empirical benchmark for Maximum Candies Allocated to K Children
"""
import time
from algorithms.practice.binary_search.max_candies_k_children import solve_max_candies_k_children

def benchmark_max_candies_k_children():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_candies_k_children([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_candies_k_children()
    print(f"Maximum Candies Allocated to K Children 100 iterations took {t*1000:.3f}ms")
